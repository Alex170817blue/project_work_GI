from flask import Blueprint, abort, jsonify, render_template, request
from sqlalchemy import inspect, text

import pipeline
from config.datasets import DATASETS
from loading.mysql_loader import mysql_connection
from webapp.jobs import JOBS, start_job

bp = Blueprint("main", __name__)
engine = mysql_connection()

STEPS = {
    "download": pipeline.run_download,
    "clean": pipeline.run_clean,
    "normalize": pipeline.run_normalize,
    "load": pipeline.run_load,
}


@bp.get("/")
def index():
    return render_template("index.html", datasets=list(DATASETS))


#esecuzione della pipeline

@bp.post("/api/run/<step>")
def run_step(step):
    if step not in STEPS:
        abort(404)
    body = request.get_json(silent=True) or {}

    kwargs = {}
    if step == "download":
        names = [n for n in body.get("datasets", []) if n in DATASETS]   # solo nomi noti
        kwargs = {
            "names": names or None,
            "force": bool(body.get("force")),
            "geo": body.get("geo") or None,
            "year_from": body.get("year_from") or None,
            "year_to": body.get("year_to") or None,
        }

    job_id = start_job(STEPS[step], **kwargs)
    if job_id is None:
        return jsonify(error="C'è già un job in esecuzione"), 409
    return jsonify(job_id=job_id)


@bp.get("/api/jobs/<job_id>")
def job_status(job_id):
    job = JOBS.get(job_id)
    if job is None:
        abort(404)
    return jsonify(job)


# dati per i grafici

def _fact_table(name):
    insp = inspect(engine)
    if not name.startswith("fact_") or name not in insp.get_table_names():
        abort(400, "Tabella non valida")
    return name, [c["name"] for c in insp.get_columns(name)]


@bp.get("/api/tables")
def tables():
    return jsonify([t for t in inspect(engine).get_table_names() if t.startswith("fact_")])


@bp.get("/api/dimensions/<table>")
def dimensions(table):
    table, cols = _fact_table(table)
    out = {}
    with engine.connect() as conn:
        for c in cols:
            if c in ("id", "value", "year"):
                continue
            rows = conn.execute(text(f"SELECT DISTINCT {c} FROM {table} ORDER BY {c}"))
            out[c] = [r[0] for r in rows]
    return jsonify(out)


@bp.get("/api/series")
def series():
    table, cols = _fact_table(request.args.get("table", ""))
    where, params = [], {}

    for col in cols:
        if col in ("id", "value", "year"):
            continue
        vals = request.args.getlist(col)
        if col != "geo" and len(vals) != 1:
            abort(400, f"Seleziona un solo valore per '{col}'")
        if vals:
            marks = []
            for i, v in enumerate(vals):
                params[f"{col}_{i}"] = v
                marks.append(f":{col}_{i}")
            where.append(f"{col} IN ({', '.join(marks)})")

    sql = f"SELECT geo, year, value FROM {table}"
    if where:
        sql += " WHERE " + " AND ".join(where)
    sql += " ORDER BY geo, year"

    result = {}
    with engine.connect() as conn:
        for geo, year, value in conn.execute(text(sql), params):
            result.setdefault(geo, []).append({"x": year, "y": value})
    return jsonify(result)
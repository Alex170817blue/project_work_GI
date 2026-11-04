import json
from pathlib import Path

import pandas as pd

STAR = Path("data/star")
SQL = Path("data/sql")
CSV = (SQL / "csv").resolve().as_posix()
SQL.mkdir(parents=True, exist_ok=True)

meta = json.loads((STAR / "_schema.json").read_text(encoding="utf-8"))
dims = [n for n in meta if n.startswith("dim_")]
facts = [n for n in meta if n.startswith("fact_")]


def sql_type(s, col):
    if pd.api.types.is_integer_dtype(s):
        return "INT"
    if pd.api.types.is_float_dtype(s):
        return "DOUBLE"
    return "VARCHAR(120)" if col.endswith("_name") or col == "geo_group" else "VARCHAR(50)"


lines = ["CREATE DATABASE IF NOT EXISTS euro_job CHARACTER SET utf8mb4;",
         "USE euro_job;",
         "SET FOREIGN_KEY_CHECKS = 0;"]
lines += [f"DROP TABLE IF EXISTS {n};" for n in dims + facts]
lines.append("SET FOREIGN_KEY_CHECKS = 1;\n")

for name in dims + facts:          
    df = pd.read_parquet(STAR / f"{name}.parquet")
    pk, fks = meta[name]["pk"], meta[name]["fks"]

    defs = [f"  {c} {sql_type(df[c], c)}{' NOT NULL' if c in pk or c in fks else ''}"
            for c in df.columns]
    defs.append(f"  PRIMARY KEY ({', '.join(pk)})")
    if pk == ["id"] and fks:
        defs.append(f"  UNIQUE KEY uq_{name} ({', '.join(fks)})")
    for col, ref in fks.items():
        table, column = ref.split(".")
        defs.append(f"  FOREIGN KEY ({col}) REFERENCES {table}({column})")

    lines.append(f"CREATE TABLE {name} (\n" + ",\n".join(defs) + "\n);\n")

(SQL / "schema.sql").write_text("\n".join(lines), encoding="utf-8")


lines = ["USE euro_job;"]
for n in dims + facts:
    lines.append(
        f"LOAD DATA LOCAL INFILE '{CSV}/{n}.csv' INTO TABLE {n} "
        "CHARACTER SET utf8mb4 FIELDS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '\"' "
        "LINES TERMINATED BY '\\r\\n' IGNORE 1 LINES;"
    )
(SQL / "load.sql").write_text("\n".join(lines), encoding="utf-8")
print("Creati data/sql/schema.sql e data/sql/load.sql")
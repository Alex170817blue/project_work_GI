from pathlib import Path
import pandas as pd
import shutil

from loading.mysql_loader import reset_mysql
from config.datasets import DATASETS
from ingestion.extract_data import download_dataset
from loading.mysql_loader import mysql_connection, load_mysql
from transformation.clean import clean_dataset
from transformation.normalize_df import build_schema, save_tables, load_tables

RAW = Path("data/raw")
CLEAN = Path("data/clean")
STAR = Path("data/star")
CSV = Path("data/sql/csv")

AGG_RULES = {
    "costo_occupazione": "mean",
    "popolazione_impiego": "mean",
    "posti_vacanti": "mean",
    "salario_minimo": "mean",
    "pil_componenti_quarto": "mean",
}


def apply_overrides(cfg, geo=None, year_from=None, year_to=None):
    cfg = {**cfg, "filters": dict(cfg["filters"])}
    f = cfg["filters"]

    if geo:
        f["geo"] = geo

    if year_from or year_to:
        temporal = dict(f.get("temporal", {}))
        quarterly = "Q" in temporal.get("sinceTimePeriod", "")
        if year_from:
            temporal["sinceTimePeriod"] = f"{year_from}-Q1" if quarterly else str(year_from)
        if year_to:
            temporal["untilTimePeriod"] = f"{year_to}-Q4" if quarterly else str(year_to)
        f["temporal"] = temporal
    return cfg


def run_download(names=None, force=False, geo=None, year_from=None, year_to=None, log=print):
    RAW.mkdir(parents=True, exist_ok=True)

    for name in (names or DATASETS):
        path = RAW / f"{name}.parquet"
        if path.exists() and not force:
            log(f"Skip (già presente): {name}")
            continue
        log(f"Download: {name}")

        try:
            cfg = apply_overrides(DATASETS[name], geo, year_from, year_to)
            df = download_dataset(cfg)
            if df.empty:
                log(f"  VUOTO: {name}, non salvato (controlla i filtri)")
                continue
            df.to_parquet(path, index=False)
            log(f"  salvato {df.shape}")
        except Exception as e:
            log(f"  ERRORE {name}: {e}")


def run_clean(log=print):
    CLEAN.mkdir(parents=True, exist_ok=True)
    for path in sorted(RAW.glob("*.parquet")):
        df = pd.read_parquet(path)
        if df.empty:
            log(f"Skip vuoto: {path.stem}")
            continue
        try:
            out = clean_dataset(df, AGG_RULES.get(path.stem))
        except Exception as e:
            log(f"ERRORE {path.stem}: {e}")
            continue
        out.to_parquet(CLEAN / path.name, index=False)
        log(f"Pulito {path.stem} {out.shape}")


def run_normalize(log=print):
    frames = {p.stem: pd.read_parquet(p) for p in sorted(CLEAN.glob("*.parquet"))}
    tables = build_schema(frames)
    save_tables(tables, STAR, csv_folder=CSV)
    for t in tables:
        log(f"{t.name}: {t.df.shape}")


def run_load(log=print):
    tables = load_tables(STAR)
    load_mysql(mysql_connection(), tables, recreate=True)
    log("Caricamento in MySQL completato")

def run_reset_db(log=print):
    reset_mysql(mysql_connection(), log=log)


def run_reset_files(log=print):
    for folder in (RAW, CLEAN, STAR, CSV.parent):
        if folder.exists():
            shutil.rmtree(folder)
            log(f"Cancellata cartella {folder}")
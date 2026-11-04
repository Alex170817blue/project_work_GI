from pathlib import Path
import pandas as pd
from transformation.normalize_df import build_schema, save_tables

CLEAN = Path("data/clean")
STAR = Path("data/star")
CSV = Path("data/sql/csv")

frames = {p.stem: pd.read_parquet(p) for p in sorted(CLEAN.glob("*.parquet"))}
tables = build_schema(frames)
save_tables(tables, STAR, csv_folder=CSV)

for t in tables:
    print(f"{t.name}: {t.df.shape} PK={t.pk}")
from pathlib import Path
import pandas as pd

from transformation.clean import clean_dataset

RAW = Path("data/raw")
CLEAN = Path("data/clean")
CLEAN.mkdir(parents=True, exist_ok=True)

RULES = {
    "costo_occupazione": "mean",
    "posti_vacanti": "mean",
    "salario_minimo": "mean",
}

for path in sorted(RAW.glob("*.parquet")):
    df = pd.read_parquet(path)

    if df.empty:
        print(f"SKIP vuoto: {path.stem}")
        continue

    try:
        out = clean_dataset(df, RULES.get(path.stem))
    except Exception as e:
        print(f"ERRORE {path.stem}: {e}")
        continue

    out.to_parquet(CLEAN / path.name, index=False)
    print(f"FATTO {path.stem} {out.shape}")

import gc
from pathlib import Path

import pandas as pd

from ingestion.eurostat_connection import EurostatConnection
from transformation.normalizer import JsonStatDataset

OUT = Path("data/raw")
OUT.mkdir(parents=True, exist_ok=True)


def download_dataset(cfg, chunk_size=7):
    filters = dict(cfg.get("filters", {}))
    filters.update(filters.pop("temporal", {}))   # temporal -> sinceTimePeriod/untilTimePeriod
    geos = filters.pop("geo", None)

    if geos is None:
        conn = EurostatConnection(cfg["dataset"], cfg["version"], filters)
        return JsonStatDataset(conn.download()).to_dataframe(use_labels=False)

    frames = []
    for i in range(0, len(geos), chunk_size):
        chunk = geos[i:i + chunk_size]
        conn = EurostatConnection(cfg["dataset"], cfg["version"], {**filters, "geo": chunk})
        frames.append(JsonStatDataset(conn.download()).to_dataframe(use_labels=False))

    return pd.concat(frames, ignore_index=True)

    

def extract_datasets(datasets):
    for name, cfg in datasets.items():
        print(f"Estrazione dataset: {name}")
        try:
            df = download_dataset(cfg)
            df.to_parquet(OUT / f"{name}.parquet", index=False)
            print(f"  salvato: {df.shape}")
            del df
            gc.collect()
        except Exception as e:
            print(f"  ERRORE nel dataset {name}: {e}")



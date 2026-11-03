from ingestion.eurostat_connection import EurostatConnection
from transformation.normalizer import JsonStatDataset
from ingestion.extract_data import download_dataset
from config.datasets import DATASETS
from pathlib import Path

OUT = Path("data/raw")
OUT.mkdir(parents=True, exist_ok=True)

for key, value in DATASETS.items():
    path = OUT / f"{key}.parquet"
    if path.exists():
        print(f"Dataset {key} already exists, skipping download.")
        continue

    print(f"Downloading dataset: {key}")
    
    try:
        df = download_dataset(value)
        df.to_parquet(f"data/raw/{key}.parquet", index=False)
        print(f"  Saved: {df.shape}")
    except Exception as e:
        print(f"  ERROR in dataset {key}: {e}")
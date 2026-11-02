
from ingestion.eurostat_connection import EurostatConnection
from transformation.normalizer import JsonStatDataset
from pathlib import Path
import gc

OUT = Path("data/raw")
OUT.mkdir(parents=True, exist_ok=True)

def download_dataset(cfg, chunk_size=7):
    filters = dict(cfg.get("filters", {}))
    geos = filters.pop("geo", None)

    if geos is None:
        conn = EurostatConnection(
            dataset=cfg["dataset"],
            version=cfg["version"],
            filters=filters)
        return JsonStatDataset(conn.download()).to_dataframe(use_labels=True)

    frames = []
    for i in range(0, len(geos), chunk_size):
        chunk = geos[i:i +chunk_size]
        conn = EurostatConnection(
            dataset=cfg["dataset"],
            version=cfg["version"],
            filters={**filters, "geo": chunk}
        )
        frames.append(JsonStatDataset(conn.download()).to_dataframe(use_labels=True))

    return pd.concat(frames, ignore_index=True)

    

def extract_datasets(datasets):
    dataframes = {}

    for name, values in datasets.items():
        print(f"Estrazione dataset: {name}")

        try:
            connection = EurostatConnection(
                dataset=values["dataset"],
                version=values["version"]
            )

            data = connection.download()
            df = JsonStatDataset(data).to_dataframe(use_labels=True)
            dataframes[name] = df
            df.to_parquet(OUT/f"{name}.parquet", index=False)

            print(f"Dataset {name} salvato, misure {df.shape}")
            del df
            gc.collect()


        except Exception as e:
            print(f"Errore nel dataset {name}: {e}")



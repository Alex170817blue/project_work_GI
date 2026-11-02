from ingestion.eurostat_connection import EurostatConnection
from transformation.normalizer import JsonStatDataset

conn = EurostatConnection("lc_lci_r2_q", version="1.0", filters={"sinceTimePeriod": "2005", "untilTimePeriod":"2025"})
ds = JsonStatDataset(conn.download())

ds.describe()                     
print(ds.dimension_values("unit"))  
df = ds.to_dataframe(use_labels=True)
print(df.head())
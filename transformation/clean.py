import pandas as pd
from config.dictionaries import GEO_NAMES

# TEMPO, GEO, UNIT, NA_ITEM, S_ADJ, NACE_R2, INDIC_EM
# TEMPO IN QUARTILI -> trasformarlo in data leggibile


def clean_time(time_series: pd.Series) -> pd.Series:
    time_series = time_series.astype(str)
    out = pd.Series(pd.NaT, index=time_series.index, dtype="datetime64[ns]")

    # Anno
    mask = time_series.str.match(r"^\d{4}")
    out[mask] = pd.to_datetime(time_series[mask], format="%Y").to_numpy()

    # Anno + trimestre
    mask = time_series.str.match(r"^\d{4}-Q[1-4]")
    out[mask] = pd.PeriodIndex(time_series[mask].str.replace("-", ""), freq="Q").to_timestamp().to_numpy()
    

    # ANNO + Semestre
    mask = time_series.str.match(r"^\d{4}-S[1-2]")
    month = time_series[mask].str[-1].map({"1":"01", "2":"07"})
    out[mask] = pd.to_datetime(time_series[mask].str[:4] + "-" + month, format="%Y-%m").to_numpy()

    return out 

def clean_geo(geo_series: pd.Series) -> pd.Series:
    return geo_series.map(GEO_NAMES).fillna(geo_series)

def clean_dataset(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    if "time" in df.columns:
        df["date"] = clean_time(df["time"])
        if df["date"].isna().any():
            bad = df.loc[df["date"].isna(), "time"].unique()[:5]
            raise ValueError(f"Formato periodo non riconosciuto: {list(bad)}")

    if "geo" in df.columns:
        df["geo_name"] = clean_geo(df["geo"])

    return df
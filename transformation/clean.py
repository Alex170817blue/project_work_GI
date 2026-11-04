import pandas as pd
from config.dictionaries import GEO_NAMES


def clean_year(time_series: pd.Series) -> pd.Series:
    s = time_series.astype(str)
    valid = s.str.fullmatch(r"\d{4}(-Q[1-4]|-S[1-2])?")
    if not valid.all():
        bad = s[~valid].unique()[:5]
        raise ValueError(f"Formato periodo non riconosciuto: {list(bad)}")
    return s.str[:4].astype(int)


def clean_geo(geo_series: pd.Series) -> pd.Series:
    return geo_series.map(GEO_NAMES).fillna(geo_series)


def to_annual(df: pd.DataFrame, how: str = "mean") -> pd.DataFrame:
    df = df.copy()
    t = df["time"].astype(str)

    if t.str.contains("-Q").all():
        n_expected = 4
    elif t.str.contains("-S").all():
        n_expected = 2
    else:
        raise ValueError("Il dataset non è tutto trimestrale o tutto semestrale")

    keys = [c for c in df.columns if c not in ("value", "time")]   # include year

    out = (
        df.groupby(keys, observed=True, dropna=False)["value"]
          .agg(value=how, n_periods="count")
          .reset_index()
    )

    incomplete = (out["n_periods"] != n_expected).sum()
    if incomplete:
        print(f"  {incomplete} righe scartate: anno incompleto")

    out = out[out["n_periods"] == n_expected].drop(columns="n_periods")
    return out.reset_index(drop=True)


def clean_dataset(df: pd.DataFrame, annual_how: str | None = None) -> pd.DataFrame:
    df = df.copy()
    df["year"] = clean_year(df["time"])

    if "geo" in df.columns:
        df["geo_name"] = clean_geo(df["geo"])

    is_annual = df["time"].astype(str).str.fullmatch(r"\d{4}").all()

    if is_annual:
        df = df.drop(columns="time")
    elif annual_how is not None:
        df = to_annual(df, annual_how)
    else:
        raise ValueError("Dataset non annuale: indica come aggregarlo ('sum' o 'mean')")

    return df
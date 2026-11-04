#costruisce colonne e dimensioni in maniera ordinata

'''
DIMENSIONALI
age, s_adj, na_item, unit, nace_r2, nace_r2_1, sizeclas
lcstruct, indic_em, currency,

NON DIMENSIONALI
geo, year, value, geo_name

DA ELIMINARE
freq, sex

FATTI
tasso, costo, inflazione, pil etc etc

------------------------------------
fatto_tasso_disocc
1 | DE | 2015 | PC | Y15-24 | 7.2

dim_geo
DE | Germania | Eurozona

dim_misure
PC | "percentuale popolazione attiva"
--------------------------------------

'''
from dataclasses import dataclass
from pathlib import Path
import pandas as pd
from sqlalchemy import  UniqueConstraint
from config.dictionaries import GEO_NAMES, DIM_NAMES, UNIT_INFO

DROP_COL = ["freq", "sex"]
DIM_COLS = ["unit", "age", "s_adj", "na_item", "nace_r2", "nace_r2_1",
            "sizeclas", "lcstruct", "indic_em"]


@dataclass
class TableStructure:
    name: str
    df: pd.DataFrame
    pk: list[str]
    fks: dict[str, str]


#CHECK DATI

def big_check(df):
    out = {}
    #droppa freq col e unisce currency e unit
    for name, dfs in df.items():
        dfs = dfs.copy()
        if "currency" in dfs.columns:
            if "unit" in dfs.columns:
                raise ValueError(f"{name}: ha sia currency sia unit, fai un check")
            dfs = dfs.rename(columns={"currency":"unit"})
        out[name] = dfs.drop(columns=[c for c in DROP_COL if c in dfs.columns])

    return out

    
def code(df, col):
    sets = [set(dfs[col].astype(str)) for dfs in df.values() if col in dfs.columns]
    return sorted(set().union(*sets)) if sets else []



#COSTRUIAMO DIMENSIONI

def build_geo(df):
    sigle = code(df, "geo")
    dfs = pd.DataFrame({
        "geo": sigle,
        "geo_name": [GEO_NAMES.get(c,c) for c in sigle]
    })

    return TableStructure("dim_geo", dfs, pk=["geo"])

def build_dim_unit(df):
    sigle = code(df, "unit")
    if not sigle:
        return None

    info = [UNIT_INFO.get(c,(c, "sconosciuto", None)) for c in sigle]
    dfs = pd.DataFrame({
        "unit":sigle,
        "unit_name": [i[0] for i in info],
        "unit_type": [i[1] for i in info],
        "base_year":pd.array([i[2] for i in info], dtype="Int64")
    })

    return TableStructure("dim_unit", dfs, pk=["unit"])

def build_year(df):
    years = sorted(set().union(*[set(df["year"].astype(int)) for dfs in df.values()]))
    return TableStructure("dim_year", pd.DataFrame({"year":years}), pk=["year"])

def build_other_dim(df, col):
    sigle = code(df, col)
    if not sigle:
        return None
    names = DIM_NAMES.get(col,{})
    dfs = pd.DataFrame({col: sigle, f"{col}":[names.get(c,c) for c in sigle]})
    return TableStructure(f"dim_{col}", dfs, pk=[col])

#COSTRUIAMO I FATTI

def build_fact(name, df):
    dims = [c for c in DIM_COLS if c in df.columns]
    key = ["geo", "year"] + dims
    fact = df[key + ["value"]].copy()
    fact["year"] = fact["year"].astype(int)

    for c in ["geo"] + dims:
        fact[c] = fact[c].astype(str)

    fact.insert(0, "id", range(1, len(fact) + 1))

    maps = {"geo":"dim_geo.geo", "year":"dim_year.year"}
    maps.update({c: f"dim_{c}" for c in dims})
    return TableStructure(f"fact_{name}", fact.reset_index(drop=True), pk=["id"], maps = maps)




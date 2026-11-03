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
tasso_disocc
DE | 2015 | PC | Y15-24 | 7.2

dim_geo
DE | Germania | Eurozona

dim_misure
PC | "percentuale popolazione attiva"
--------------------------------------

'''
from dataclasses import dataclass
from pathlib import Path
import pandas as pd
from transformation.clean import GEO_NAMES

DIM_NAMES = {

    "sex": {"T": "Totale", "M":"Uomini", "F":"Donne"},
    "age": {"Y15-24": "15-24 anni", "Y25-54": "25-54 anni", "Y55-64":"55-64 anni"},
    "s_adj":{"NSA":"Dati non destagionalizzati"}, #da allargare se vogliamo altri dati con filtri diversi
    "nace_r2":{
        "A": "Agricoltura, Silvicoltura e pesca",
        "B-E" : "Industria (escluse costruzioni)",
        "C" : "Attività manifatturiere",
        "F": "Costruzioni",
        "G-I": "Commercio, trasporti, alloggio e ristorazione",
        "G-J": "Commercio, trasporti, alloggio, informazione e ristorazione",
        "J": "Informazione e comunicazione",
        "K": "Attività finanziarie e assicurative",
        "L":"Attività immobiliari",
        "M-N":"Attività professionali e servizi di supporto",
        "K-N": "Finanza, immobiliare e servizi alle imprese",
        "O-Q":"Pubblica amministrazione, istruzione e sanità",
        "O-S":"Pubblica amministrazione e altri servizi",
        "R-U": "Arte, intrattenimento e altri servizi",
        "B-S":"Economia (escl. agricoltura e famiglie)"
    },

    "na_item":{
        "B1G":"Valore Aggiunto lordo",
        "EMP_DC":"O"},

    "indic_em": {}

}

DROP_COL = ["freq"]

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

    #DA FARE DIZIONARIO
    info = [UNITA_INFO.get(c,(c, "sconosciuto", None)) for c in sigle]
    dfs = pd.DataFrame({
        "unit":sigle,
        "unit_name": [i[0] fori in info],
        ...
    })

    return TableStructure("dim_unit", dfs, pk=["unit"])

def build_other_dim(df, col):
    sigle = code(df, col)
    if not sigle:
        return None
    names = DIM_NAMES.get(col,{})
    dfs = pd.DataFrame({col: sigle, f"{col}":[names.get(c,c) for c in sigle]})
    return TableStructure(f"dim_{col}", dfs, pk=[col])



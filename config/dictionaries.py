#NOMI LEGGIBILI DIMENSIONI

DIM_NAMES = {

    "sex": {"T": "Totale", "M":"Uomini", "F":"Donne"},
    
    "age": {"Y15-24": "15-24 anni", "Y25-54": "25-54 anni", "Y55-64":"55-64 anni"},
    
    "s_adj":{"NSA":"Dati non destagionalizzati",
            "SA": "Destagionalizzati",
            "SCA": "Destagionalizzati e corretti per i giorni lavorativi",
            "CA": "Corretti per i giorni lavorativi"
        }, #da allargare se vogliamo altri dati con filtri diversi
    
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
        "B-S":"Economia (escl. agricoltura e famiglie)",
        "B-S_X_O": "Economia di mercato (escl. agricoltura e pubblica amministrazione)",
        "B-N": "Industria e servizi di mercato",
    },
    

    "na_item": {
        "B1GQ": "PIL ai prezzi di mercato",
        "B1G": "Valore aggiunto lordo",
        "EMP_DC": "Occupati (concetto interno)",
        "SAL_DC": "Lavoratori dipendenti (concetto interno)",
        "SELF_DC": "Lavoratori autonomi (concetto interno)",
        "D1": "Redditi da lavoro dipendente",
    },
    "indic_em": {
        "JOBRATE": "Tasso di posti vacanti",
        "JOBVAC": "Numero di posti vacanti",
        "EMP_LFS": "Occupati (indagine forze lavoro)",
    },
    "coicop": {
        "CP00": "Tutti i beni e servizi",
        "CP01": "Alimentari e bevande analcoliche",
        "CP04": "Abitazione, acqua, elettricità e combustibili",
        "CP07": "Trasporti",
    },
    "lcstruct": {
        "D1_D4_MD5": "Costo totale del lavoro",
        "D11": "Salari e stipendi",
        "D12_D4_MD5": "Contributi sociali e altri costi non salariali",
    },
}

#DIZIONARIO UNITà
UNIT_INFO = {
    # indici
    "I20": ("Indice (2020 = 100)", "indice", 2020),
    "I16": ("Indice (2016 = 100)", "indice", 2016),
    "I15": ("Indice (2015 = 100)", "indice", 2015),
    "CLV_I20": ("Indice dei volumi concatenati (2020 = 100)", "indice", 2020),
    # variazioni percentuali
    "PCH_SM": (f"Variazione % sullo stesso periodo dell'anno precedente", "variazione_pct", None),
    "PCH_PRE": (f"Variazione % sul periodo precedente", "variazione_pct", None),
    "PCH_PRE_PER": (f"Variazione % sul periodo precedente", "variazione_pct", None),
    "PCH_SM_PER": (f"Variazione % sullo stesso periodo dell'anno precedente", "variazione_pct", None),
    "RCH_A_AVG": ("Tasso di variazione medio annuo", "variazione_pct", None),
    # valori in euro
    "CP_MEUR": ("Milioni di euro, prezzi correnti", "valore_corrente", None),
    "CLV20_MEUR": ("Milioni di euro, volumi concatenati (2020)", "volume_concatenato", None),
    "CLV10_MEUR": ("Milioni di euro, volumi concatenati (2010)", "volume_concatenato", None),
    # persone e ore
    "THS_PER": ("Migliaia di persone", "persone", None),
    "THS_HW": ("Migliaia di ore lavorate", "ore", None),
    # percentuali
    "PC": ("Percentuale", "percentuale", None),
    "PC_ACT": (f"% della popolazione attiva", "percentuale", None),
    "PC_POP": (f"% della popolazione", "percentuale", None),
    # valute (currency di earn_mw_cur, trattata come unità)
    "EUR": ("Euro", "valuta", None),
    "PPS": ("Standard di potere d'acquisto (PPS)", "valuta", None),
    "NAC": ("Valuta nazionale", "valuta", None),
}


GEO_NAMES = {
    "EU27_2020": "Unione Europea (UE27)",
    "EA20": "Eurozona (EA20)",
    "AT": "Austria",
    "BE": "Belgio",
    "BG": "Bulgaria",
    "CY": "Cipro",
    "CZ": "Repubblica Ceca",
    "DE": "Germania",
    "DK": "Danimarca",
    "EE": "Estonia",
    "EL": "Grecia",
    "ES": "Spagna",
    "FI": "Finlandia",
    "FR": "Francia",
    "HR": "Croazia",
    "HU": "Ungheria",
    "IE": "Irlanda",
    "IT": "Italia",
    "LT": "Lituania",
    "LU": "Lussemburgo",
    "LV": "Lettonia",
    "MT": "Malta",
    "NL": "Paesi Bassi",
    "PL": "Polonia",
    "PT": "Portogallo",
    "RO": "Romania",
    "SE": "Svezia",
    "SI": "Slovenia",
    "SK": "Slovacchia"
}
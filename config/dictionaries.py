#NOMI LEGGIBILI DIMENSIONI

DIM_NAMES = {

    "sex": {"T": "Totale", "M":"Uomini", "F":"Donne"},
    
    "age": {"Y15-24": "15-24 anni", "Y25-54": "25-54 anni", "Y55-64":"55-64 anni"},
    
    "s_adj":{
            "NSA":"Dati non destagionalizzati",
            "SA": "Destagionalizzati",
            "SCA": "Destagionalizzati e corretti per i giorni lavorativi",
            "CA": "Corretti per i giorni lavorativi"
        }, #da allargare se vogliamo altri dati con filtri diversi
    
    "nace_r2":{
        "A": "Agricoltura, silvicoltura e pesca",
        "B": "Estrazione di minerali da cave e miniere",
        "B-E": "Industria (escluse costruzioni)",
        "B-F": "Industria e costruzioni",
        "B-N": "Industria e servizi di mercato",
        "B-S": "Economia (esclusa agricoltura e famiglie)",
        "C": "Attività manifatturiere",
        "D": "Fornitura di energia elettrica, gas e vapore",
        "E": "Fornitura di acqua e gestione dei rifiuti",
        "F": "Costruzioni",
        "G": "Commercio all'ingrosso e al dettaglio",
        "G-I": "Commercio, trasporti, alloggio e ristorazione",
        "G-J": "Commercio, trasporti, alloggio, ristorazione e informazione",
        "G-N": "Servizi di mercato",  # verifica
        "H": "Trasporto e magazzinaggio",
        "I": "Alloggio e ristorazione",
        "J": "Informazione e comunicazione",
        "K": "Attività finanziarie e assicurative",
        "K-N": "Finanza, immobiliare e servizi alle imprese",
        "L": "Attività immobiliari",
        "M": "Attività professionali, scientifiche e tecniche",
        "M_N": "Attività professionali e servizi di supporto",
        "N": "Attività amministrative e di servizi di supporto",
        "O": "Pubblica amministrazione e difesa",
        "O-Q": "Pubblica amministrazione, istruzione e sanità",
        "O-S": "Pubblica amministrazione e altri servizi",
        "P": "Istruzione",
        "Q": "Sanità e assistenza sociale",
        "R": "Arte, intrattenimento e divertimento",
        "R-U": "Arte, intrattenimento e altri servizi",
        "S": "Altre attività di servizi",
    },
    

    "na_item": {
        "B1GQ": "PIL ai prezzi di mercato",
        "B1G": "Valore aggiunto lordo",
        "B2A3G": "Risultato lordo di gestione e reddito misto",
        "D1": "Redditi da lavoro dipendente",
        "D11": "Retribuzioni lorde",
        "D12": "Contributi sociali a carico dei datori di lavoro",
        "D1_SAL_HW": "Redditi da lavoro dipendente per ora lavorata",  # verifica
        "D2": "Imposte sulla produzione e sulle importazioni",
        "D21": "Imposte sui prodotti",
        "D21X31": "Imposte sui prodotti al netto dei contributi ai prodotti",
        "D2X3": "Imposte sulla produzione e importazioni al netto dei contributi",
        "D3": "Contributi alla produzione e alle importazioni",
        "D31": "Contributi ai prodotti",
        "EMP_DC": "Occupati (concetto interno)",
        "SAL_DC": "Lavoratori dipendenti (concetto interno)",
        "SELF_DC": "Lavoratori autonomi (concetto interno)",
        "P3": "Spesa per consumi finali",
        "P31_S13": "Consumi individuali delle amministrazioni pubbliche",
        "P31_S14": "Consumi individuali delle famiglie",
        "P31_S14_S15": "Consumi individuali di famiglie e ISP",
        "P31_S15": "Consumi individuali delle istituzioni senza scopo di lucro",
        "P32_S13": "Consumi collettivi delle amministrazioni pubbliche",
        "P3_P5": "Domanda interna (consumi e investimenti)",
        "P3_P6": "Consumi finali ed esportazioni", 
        "P3_S13": "Consumi finali delle amministrazioni pubbliche",
        "P41": "Consumi finali effettivi individuali",
        "P51G": "Investimenti fissi lordi",
        "P52": "Variazione delle scorte",
        "P52_P53": "Variazione delle scorte e oggetti di valore",
        "P53": "Acquisizioni meno cessioni di oggetti di valore",
        "P5G": "Formazione lorda di capitale",
        "P6": "Esportazioni di beni e servizi",
        "P61": "Esportazioni di beni",
        "P61X71": "Saldo commerciale dei beni",
        "P62": "Esportazioni di servizi",
        "P62X72": "Saldo commerciale dei servizi",
        "P6X7": "Saldo delle esportazioni nette di beni e servizi",
        "P7": "Importazioni di beni e servizi",
        "P71": "Importazioni di beni",
        "P72": "Importazioni di servizi",
        "YA0": "Discrepanza statistica (lato spesa)", 
        "YA1": "Domanda finale interna", 
        "YA2": "Usi finali"
    },

    "indic_em": {
        "ACT": "Popolazione attiva",
        "EMP_LFS": "Occupati (indagine forze lavoro)",
        "JVR": "Tasso di posti vacanti",
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
        "D1_D4_MD5_XB": "Costo totale del lavoro (escluse le retribuzioni variabili)",
        "D11": "Salari e stipendi",
        "D12_D4_MD5": "Contributi sociali e altri costi non salariali",
    },

    "sizeclas":{
        "GE10":"Imprese con 10 dipendenti e oltre",
        "TOTAL":"Tutte le imprese"
    }
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
    "PC_TOT_HW": (f"% del totale delle ore lavorate", "percentuale", None),
    "PC_TOT_JOB": (f"% del totale dei posti di lavoro", "percentuale", None),
    "PC_TOT_PER": (f"% del totale delle persone occupate", "percentuale", None),
    # valute (currency di earn_mw_cur, trattata come unità)
    "EUR": ("Euro", "valuta", None),
    "PPS": ("Standard di potere d'acquisto (PPS)", "valuta", None),
    "NAC": ("Valuta nazionale", "valuta", None),
    "PPS_EU27_2020":("Standard di potere d'acquisto (base UE27 dal 2020)", "valuta", None)
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
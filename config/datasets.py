from config.filters import ANNUALE, TRIMESTRALE, GEO_ALL, SEX, AGE

'''DA AGGIORNARE CON I FILTRI'''

DATASETS = {
    # costo occupazione per impresa
    '''I20 = indice con anno di riferimento 2020
    PCH_SM = variazione percentuale rispetto allo stesso
    periodo dell'anno precedente (da verificare nel dataset)
    NSA = dati non corretti per effetti stagionali '''

    "costo_occupazione":{
        "version": "1.0",
        "dataset": "lc_lci_r2_q",
        "filters": {
            "geo": GEO_ALL,
            "temporal": TRIMESTRALE,
            "unit": ["I20", "PCH_SM"],
            "s_adj": ["NSA"],
            "nace_r2": "TOTAL", #da verificare se A è il totale
            "sex": SEX,
            "age": AGE
        }
    },

    # tasso di disoccupazione/occupazione
    "tasso_disoccupazione":{
        "version": "1.0",
        "dataset": "une_rt_a",
        "filters": {
            "geo": GEO_ALL,
            "temporal": ANNUALE,
            "sex": SEX,
            "age": AGE
        }
    },

    "tasso_occupazione":{
        "version": "1.0",
        "dataset": "lfsi_emp_a",
        "filters": {
            "geo": GEO_ALL,
            "temporal": ANNUALE,
            "sex": SEX,
            "age": AGE
        }
    },

    # occupazione per settore
    "occupazione_settore_92":{
        "version": "1.0",
        "dataset": "lfsa_egana",
        "filters": {
            "geo": GEO_ALL,
            "temporal": ANNUALE,
            "sex": SEX,
            "age": AGE,
            "nace_r2": "TOTAL"
        }
    },
    
    
    "occupazione_settore_08":{
        "version": "1.0",
        "dataset": "lfsa_egan22d",
        "filters": {
            "geo": GEO_ALL,
            "temporal": ANNUALE,
            "sex": SEX,
            "age": AGE,
            "nace_r2": "TOTAL"
        }
    },

    #posti vacanti per settore
    ''' A-T = aggregato delle attività economiche
    NSA = dati non destagionalizzati
    JVR = job vacancy rate, tasso di posti vacanti'''

    "posti_vacanti":{
        "version":"1.0",
        "dataset":"jvs_q_r21",
        "filters": {
            "geo": GEO_ALL,
            "temporal": ANNUALE,
            "sex": SEX,
            "age": AGE,
            "nace_r2": "A-T",
            "s_adj": "NSA",
            "indic_em": "JVR"
        }
    },

    #confronto pil e mercato del lavoro
    #nota primo lc_lci_r2_q + lfsi_emp_a

    #produttività del lavoro
    ''' CLV = chain-linked volumes, volumi concatenati
    I20 = anno di riferimento 2020
    Usato per analizzare il PIL reale
    B1G = prodotto interno lordo ai prezzi di mercato '''

    "pil_componenti_anno": {
        "version":"1.0",
        "dataset":"nama_10_gdp",
        "filters": {
            "geo": GEO_ALL,
            "temporal": ANNUALE,
            "unit":"CLV120",
            "na_item":"B1G"

        }
    },

    '''CP_MEUR = prezzi correnti in milioni di euro
    Usato per analizzare il PIL nominale
    B1G = prodotto interno lordo ai prezzi di mercato '''

    "pil_nominale_anno": {
            "version":"1.0",
            "dataset":"nama_10_gdp",
            "filters": {
                "geo": GEO_ALL,
                "temporal": ANNUALE,
                "unit":"CP_MEUR",
                "na_item":"B1G"
    
            }
        },

    #occupazione per attività economica
    '''CLV10_MEUR = chain-linked volumes, volumi concatenati
    serve per confrontare il PIL reale tra paesi senza le fluttuazioni dei tassi di cambio
    B1G = prodotto interno lordo ai prezzi di mercato
    '''

    "occupazione_per_attività":{
        "version":"2.0",
        "dataset":"nama_10_a10_e",    
        "filters": {
            "geo": GEO_ALL,
            "temporal": ANNUALE,
            "unit":"CLV10_MEUR",
            "na_item":"B1G"
        }
    },

    "produttivita_costo_lavoro": {
        "version":"2.0",
        "dataset":"nama_10_lp_ulc",
        "filters": {
            "geo": GEO_ALL,
            "temporal": ANNUALE,
            "unit":"CLV10_MEUR",
            "na_item":"B1G",
        }
    },

    #disparità tra eurozona e paesi fuori
    '''CLV120 valori a volumi concatenati con anno di riferimento 2020
    serve per confrontare il PIL reale tra paesi senza le fluttuazioni dei tassi di cambio'''

    "pil_componenti_quarto":{
        "version":"1.0",
        "dataset": "namq_10_gdp",
        "filters": {
            "geo": GEO_ALL,
            "temporal": TRIMESTRALE,
            "unit":"CLV120",
            "na_item":"B1G",
            "s_adj":"NSA"        
        }
    },

    '''PCH_PRE_PER = variazione percentuale rispetto allo stesso periodo dell'anno 
    precedente'''

    "popolazione_impiego":{
        "version":"2.0",
        "dataset":"namq_10_pe",
        "filters": {
            "geo": GEO_ALL,
            "temporal": TRIMESTRALE,
            "unit":"PCH_PRE_PER",
            "na_item":"B1G",
            "s_adj":"NSA"
        }

    },

    #per disoccupazione annuale guarda une_rt_a

    #salari reali e potere d'acquisto: nama_10_lp_ul
    '''rch_a_avg = valori medi a prezzi correnti
    CP00 all items, tutti i beni e servizi'''

    "produttivita_costo_lavoratori":{
        "version":"1.0",
        "dataset":"prc_hicp_aind",
        "filters": {
            "geo": GEO_ALL,
            "temporal": ANNUALE,
            "unit":"RCH_A_AVG",
            "coicop":"CP00"
        }
    },

    '''PPS = parità di potere d'acquisto, valuta standardizzata per 
    confrontare il potere d'acquisto tra paesi
    EUR = euro'''
    "salario_minimo":{
        "version":"1.0",
        "dataset":"earn_mw_cur",
        "filters": {
            "geo": GEO_ALL,
            "temporal": ANNUALE,
            "currency":["PPS", "EUR"]
        }
    }

}

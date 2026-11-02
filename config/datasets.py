from config.filters import ANNUALE, TRIMESTRALE, GEO_ALL, SEX, AGE

'''DA AGGIORNARE CON I FILTRI'''

DATASETS = {
    # costo occupazione per impresa
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
    "pil_componenti_anno": {
        "version":"1.0",
        "dataset":"nama_10_gdp",
        "filters": {"sinceTimePeriod": "2005", "untilTimePeriod":"2025"}
    },

    "nama_10":{
        "version":"2.0",
        "dataset":"nama_10_a10_e"    
    },

    "produttivita_costo_lavoro": {
        "version":"2.0",
        "dataset":"nama_10_lp_ulc",
        "filters": {"sinceTimePeriod": "2005", "untilTimePeriod":"2025"}
    },

    #disparità tra eurozona e paesi fuori
    "pil_componenti_quarto":{
        "version":"1.0",
        "dataset": "namq_10_gdp",
        "filters": {"sinceTimePeriod": "2005", "untilTimePeriod":"2025"}
    },

    "namq_10_pe":{
        "version":"2.0",
        "dataset":"namq_10_pe",
        "filters": {"sinceTimePeriod": "2005", "untilTimePeriod":"2025"}

    },

    #per disoccupazione annuale guarda une_rt_a

    #salari reali e potere d'acquisto: nama_10_lp_ulc
    "produttivita_costo_lavoratori":{
        "version":"1.0",
        "dataset":"prc_hicp_aind",
        "filters": {"sinceTimePeriod": "2005", "untilTimePeriod":"2025"}
    },

    "salario_minimo":{
        "version":"1.0",
        "dataset":"earn_mw_cur",
        "filters": {"sinceTimePeriod": "2005", "untilTimePeriod":"2025"}
    }

}

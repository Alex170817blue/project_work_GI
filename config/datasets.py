from config.filters import ANNUALE, TRIMESTRALE, GEO_ALL, SEX, AGE


DATASETS = {
    # costo occupazione per impresa

    "costo_occupazione":{
        "version": "1.0",
        "dataset": "lc_lci_r2_q",
        "filters": {
            "geo": GEO_ALL,
            "temporal": TRIMESTRALE,
            "unit": ["PCH_SM","I20"],
            "s_adj": "NSA",
            "lcstruct": ["D1_D4_MD5", "D11", "D12_D4_MD5"],
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
    # "occupazione_settore_92":{
    #     "version": "1.0",
    #     "dataset": "lfsa_egana",
    #     "filters": {
    #         "geo": GEO_ALL,
    #         # "temporal": ANNUALE,
    #         "sex": SEX,
    #         "age": AGE,
    #         "nace_r2": "TOTAL"
    #     }
    # },
    
    
    # "occupazione_settore_08":{
    #     "version": "1.0",
    #     "dataset": "lfsa_egan22d",
    #     "filters": {
    #         "geo": GEO_ALL,
    #         "temporal": ANNUALE,
    #         "sex": SEX,
    #         "age": AGE,
    #         "nace_r2": "TOTAL"
    #     }
    # },

    #posti vacanti per settore
  

    "posti_vacanti":{
        "version":"1.0",
        "dataset":"jvs_q_r21",
        "filters": {
            "geo": GEO_ALL,
            "temporal": ANNUALE,
            "nace_r2_1": "A-T",
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
        "filters": {
            "geo": GEO_ALL,
            "temporal": ANNUALE,
            "unit":"CLV20_MEUR",
            "na_item":"B1GQ"

        }
    },

    "pil_nominale_anno": {
            "version":"1.0",
            "dataset":"nama_10_gdp",
            "filters": {
                "geo": GEO_ALL,
                "temporal": ANNUALE,
                "unit":"CP_MEUR",
                "na_item":"B1GQ"

            }
        },

    #occupazione per attività economica


    "occupazione_per_attivita":{
        "version":"1.0",
        "dataset":"nama_10_a10_e",    
        "filters": {
            "geo": GEO_ALL,
            "temporal": ANNUALE,
            "unit":["PC_TOT_PER", "PC_TOT_HW", "PC_TOT_JOB", "THS_PER"],
            "nace_r2": ["TOTAL", "A", "B-E", "F", "G-I", "J", "K", "L", "M_N", "O-Q", "R-U"],
        }
    },

    "produttivita_costo_lavoro": {
        "version":"1.0",
        "dataset":"nama_10_lp_ulc",
        "filters": {
            "geo": GEO_ALL,
            "temporal": ANNUALE,
            "unit":"PPS_EU27_2020",
            "na_item":"D1_SAL_HW",
        }
    },

    #disparità tra eurozona e paesi fuori

    "pil_componenti_quarto":{
        "version":"1.0",
        "dataset": "namq_10_gdp",
        "filters": {
            "geo": GEO_ALL,
            "temporal": TRIMESTRALE,
            "unit":"CLV_I20",
            "na_item":"B1G",
            "s_adj":"NSA"        
        }
    },


    "popolazione_impiego":{
        "version":"1.0",
        "dataset":"namq_10_pe",
        "filters": {
            "geo": GEO_ALL,
            "temporal": TRIMESTRALE,
            "na_item":"EMP_DC",
            "unit":"THS_PER",
            "s_adj":"NSA",
        }
    },

    #per disoccupazione annuale guarda une_rt_a

    #salari reali e potere d'acquisto: nama_10_lp_ul


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


    "salario_minimo":{
        "version":"1.0",
        "dataset":"earn_mw_cur",
        "filters": {
            "geo": GEO_ALL,
            "temporal": ANNUALE,
            "currency":["PPS", "EUR"],
        }
    }

}

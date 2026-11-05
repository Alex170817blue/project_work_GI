# EUROSTAT PIPELINE
pipeline di analisi dati, in questo caso focalizzata sul mercato del lavoro europeo (2005-2025). I dati sono presi da Eurostato open data e vengono aggregati annualmente.

## Architettura
```
Eurostat API (JSON-stat)
   │  ingestion/        download con filtri, in chunks di paesi per evitare overload
   ▼
data/raw/*.parquet      raw data
   │  transformation/clean.py       aggregazione annuale
   ▼
data/clean/*.parquet
   │  transformation/normalize_df.py creazione di schema a stella
   ▼
data/star/*.parquet + _schema.json + CSV
   │                        SQLAlchemy + creazione csv
   ▼
MySQL
```
## Decisioni architetturali

- JSON-stat "sparse": vengono convertite solo le celle esistenti, evitando di esaurire la memoria con prodotti cartesiani
- **Aggregazione temporale**Le serie trimestrali e semestrali venfono aggregate in anni, gli anni incompleti vengono scartati

## Come Usarlo
in ordine, esegui

```bash
python extract_all.py     # download raw data
python clean_all.py       # pulisce e aggrega
python normalize_all.py   # costruisce lo schema a stella
python make_sql.py        # crea lo script sql
```

## Come Contribuire

### Prerequisiti
- Git
- Python 3.10 o >>
- MySQL 8
- Un account Github 

### Primi step

Ricordati, se sei un contributore esterno, clicca **'Fork'** in alto a destra per _forcare_ la repository e poi clona la tua _forchetta_

```bash
git clone https://github.com/Alex170817blue/project_work_GI.git
cd project_work_GI
```

**SOLO PER CONTRIBUTORI ESTERNI** aggiungi l'orgiinale come 'upstream', in vista di futuri pull

```bash
git remote add upstream https://github.com/Alex170817blue/project_work_GI.git
git remote -v
```

### Setup

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Crea la tua branch

Per evitare conflitti è bene lavorare ciascuno sulla propria branch! Prima però sii sicuro di avere tutti gli aggiornamenti del developing. Il main NON SI TOCCA

```bash
git checkout developing
git pull origin developing    # or "git pull upstream main" se sei esterno
```
Ora crea la tua branch!

```bash
git checkout -b feature/short-description
```

"feature" è per convenzione una branch dove puoi aggiungere nuove funzionalità, dataset diversi e analisi particolari. oltre a feature, nomina la tua branch con una brevissimissima descrizione (es. MioNome_datasetpersesso).

**Altri nomi convenzionali delle branch sono:**
- fix/ -> per aggiustare problemi
- docs/ -> per la documentazione
- refactor/ -> cambi il codice, ma non cambia il comportamento del programma

### Divertiti e sviluppa
Ora tocca a te! Cambia il dataset, il codice o quello che preferisci, ma non dimenticarti: ad ogni cambiamento...

```bash
git status
git add transformation/clean.py config/datasets.py
git commit -m "Add quarterly unemployment dataset"
git push origin feature/short-description
```

Non dimenticarti ogni tanto di controllare che non cambi il main:
```bash
git fetch origin
git merge developing    # or: git merge upstream/developing
```

## Common problems

| Problem | Solution |
|---|---|
| `ModuleNotFoundError` | env non attivo o non sei nella directory giusta |
| Eurostat returns 404 or 400 |un filtro in `config/datasets.py` non esiste per quel dataset o è scritto sbagliato |
| Eurostat returns 413 | La richiesta è troppo grande! aggiungi dei filtri al dataset o riduci la chunk_size |
| `Dataset non annuale` error | aggiungi il dataset as `AGG_RULES` in `clean_all.py`. |
| MySQL "Loading local data is disabled" |  enable `local_infile`sia su server che su client da CLI |

### Sviluppi Futuri
- **Interfaccia Web con Flask:** Sviluppare una GUI web per permettere all'utente di avviare la pipeline, selezionare i filtri dei dataset e visualizzare i grafici.
- **Orchestrare con Apache Airflow:** Automatizzare e monitorare periodicamente l'intera pipeline di acquisizione e trasformazione dati.
- **Analisi Predittiva:** Approfondire lo studio delle metriche del mercato del lavoro attraverso modelli statistici e previsionali (Machine Learning).


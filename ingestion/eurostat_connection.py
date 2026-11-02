import requests


class EurostatConnection:
    url_base = "https://ec.europa.eu/eurostat/api/dissemination/statistics/{version}/data/{dataset}"

    def __init__(self, dataset: str, version: str = "1.0", filters: dict | None = None):
        self.dataset = dataset
        self.url = self.url_base.format(version=version, dataset=dataset)
        self.params = {"format": "JSON", "lang": "en"}
        self.params.update(filters or {}) 

    def download(self):
        response = requests.get(self.url, params=self.params, timeout=120)
        response.raise_for_status()
        return response.json()

'''
Oggetto: EurostatConnection
Questa classe permette di connettersi all'API di Eurostat per scaricare dati statistici in formato JSON
la funzione extract_data() permetterà poi di estrarre i dati dal JSON.
'''
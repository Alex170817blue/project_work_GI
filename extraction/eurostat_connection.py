import requests

class EurostatConnection:
    url_base = "https://ec.europa.eu/eurostat/api/dissemination/statistics/{version}/data/{dataset}?format=json&lang=en"

    def __init__(self, dataset: str, version: str = "1.0"):
        self.dataset = dataset
        self.version = version
        self.url = self.url_base.format(version=self.version, dataset=self.dataset)

    def download(self):
        response = requests.get(self.url, params={"format": "json", "lang": "en"})
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

'''
Oggetto: EurostatConnection
Questa classe permette di connettersi all'API di Eurostat per scaricare dati statistici in formato JSON
la funzione extract_data() permetterà poi di estrarre i dati dal JSON.
'''
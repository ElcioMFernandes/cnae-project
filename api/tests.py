import pandas as pd
import requests as req

class Test:
    def __init__(self, spreadsheet):
        self.df = pd.read_excel(spreadsheet)
        self.coluna_url = {
            'CD_SECAO': 'http://localhost:8000/secoes/',
            'CD_DIVISAO': 'http://localhost:8000/divisoes/',
            'CD_GRUPO': 'http://localhost:8000/grupos/',
            'CD_CLASSE': 'http://localhost:8000/classes/',
            'CD_SUBCLASSE': 'http://localhost:8000/subclasses/'
        }

    def get(self, url, param):
        response = req.get(f"{url}{param}/")
        return response
    
    def main(self):
        for url_key, url_value in self.coluna_url.items():
            coluna = sorted(set(self.df[url_key]))
            for coluna_index, coluna_value in enumerate(coluna):
                response = self.get(url_value, coluna_value)
                if response.text == 'Not Found':
                    print(f"{url_key} not found: {coluna_value}")
                    break
                    exit()
                else:
                    print(coluna_index)

teste_api = Test('spreadsheets/setor_economico_ajustado.xlsx')
teste_api.main()

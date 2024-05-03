import requests, pandas as pd

class Request:

    ## Referente ao conteúdo do arquivo excel
    dataframe = None # Datafram com os dados do arquivo excel

    ## Referente as rotas da API e do IBGE
    ibge_secao = 'https://servicodados.ibge.gov.br/api/v2/cnae/secoes' #Retornar todas as seções
    ibge_secao_por_identificador = 'https://servicodados.ibge.gov.br/api/v2/cnae/secoes/{secao}' #Retorna uma seção pelo seu identificador
    
    ibge_divisao = 'https://servicodados.ibge.gov.br/api/v2/cnae/divisoes' #Retornar todas as divisões
    ibge_divisao_por_identificador = 'https://servicodados.ibge.gov.br/api/v2/cnae/divisoes/{divisao}' #Retorna uma divisão pelo seu identificador
    ibge_divisao_por_setor = 'https://servicodados.ibge.gov.br/api/v2/cnae/secoes/{secao}/divisoes' #Retorna todas as divisões de uma seção

    ibge_grupo = 'https://servicodados.ibge.gov.br/api/v2/cnae/grupos' #Retornar todos os grupos
    ibge_grupo_por_identificador = 'https://servicodados.ibge.gov.br/api/v2/cnae/grupos/{grupo}' #Retorna um grupo pelo seu identificador
    ibge_grupo_por_divisao = 'https://servicodados.ibge.gov.br/api/v2/cnae/divisoes/{divisao}/grupos' #Retorna todos os grupos de uma divisão

    ibge_classe = 'https://servicodados.ibge.gov.br/api/v2/cnae/classes' #Retornar todas as classes
    ibge_classe_por_identificador = 'https://servicodados.ibge.gov.br/api/v2/cnae/classes/{classe}' #Retorna uma classe pelo seu identificador
    ibge_classe_por_grupo = 'https://servicodados.ibge.gov.br/api/v2/cnae/grupos/{grupo}/classes'
        
    ibge_subclasse = 'https://servicodados.ibge.gov.br/api/v2/cnae/subclasses' #Retornar todas as subclasses
    ibge_subclasse_por_identificador = 'https://servicodados.ibge.gov.br/api/v2/cnae/subclasses/{subclasse}' #Retorna uma subclasse pelo seu identificador
    ibge_subclasse_por_classe = 'https://servicodados.ibge.gov.br/api/v2/cnae/classes/{classe}/subclasses' #Retorna todas as subclasses de uma classe

    ## Referente as rotas da API
    api_secao = 'http://127.0.0.1:{port}/secoes/' #Inserir uma seção
    api_divisao = 'http://127.0.0.1:{port}/divisoes/' #Inserir uma divisão
    api_grupo = 'http://127.0.0.1:{port}/grupos/' #Inserir um grupo
    api_classe = 'http://127.0.0.1:{port}/classes/' #Inserir uma classe
    api_subclasse = 'http://127.0.0.1:{port}/subclasses/' #Inserir uma subclasse
    api_arrecadacao = 'http://127.0.0.1:{port}/arrecadacoes/' #Inserir uma arrecadação

    ## Exemplo de dados para inserção
    #     {
    #     "vl_arrecadacao": null, -> Valor da arrecadação tipo float
    #     "id_divisao_setor": null, -> Identificador da divisão do setor tipo int
    #     "id_setor_economico": null, -> Identificador do setor econômico tipo int
    #     "id_data": null, -> Identificador da data tipo int
    #     "id_subclasse": null -> Identificador da subclasse tipo int
    # }

    def __init__(self, spreadsheet, port=8000):
        """Por padrão o construtor recebe a porta 8000, caso deseje alterar a porta informe-a como parâmetro"""
        self.api_secao = self.api_secao.format(port=port)
        self.api_divisao = self.api_divisao.format(port=port)
        self.api_grupo = self.api_grupo.format(port=port)
        self.api_classe = self.api_classe.format(port=port)
        self.api_subclasse = self.api_subclasse.format(port=port)
        self.api_arrecadacao = self.api_arrecadacao.format(port=port)
        self.dataframe = pd.read_excel(spreadsheet)
    
    def get_ibge_secao(self):
        """Retorna todas as seções do IBGE"""
        return requests.get(self.ibge_secao).json()
    
    def get_ibge_secao_por_identificador(self, identificador):
        """Retorna uma seção do IBGE pelo seu identificador\nParâmetros:\n- identificador: Identificador da seção"""
        return requests.get(f"{self.ibge_secao_por_identificador}{identificador}").json()
    
    def get_ibge_divisao(self):
        """Retorna todas as divisões do IBGE"""
        return requests.get(self.ibge_divisao).json()
    
    def get_ibge_divisao_por_identificador(self, identificador):
        """Retorna uma divisão do IBGE por um identificador\nParâmetros:\n- identificador: Identificador da divisão"""
        return requests.get(f"{self.ibge_divisao_por_identificador}{identificador}").json()
    
    def get_ibge_divisao_por_secao(self, secao):
        """Retorna todas as divisões de uma seção\nParâmetros:\n- secao: Código da seção"""
        return requests.get(f"{self.ibge_divisao_por_setor.format(secao=secao)}").json()

    def get_ibge_grupo(self):
        """Retorna todos os grupos do IBGE"""
        return requests.get(self.ibge_grupo).json()
    
    def get_ibge_grupo_por_identificador(self, identificador):
        """Retorna um grupo do IBGE por um identificador\nParâmetros:\n- identificador: Identificador do grupo"""
        return requests.get(f"{self.ibge_grupo_por_identificador}{identificador}").json()
    
    def get_ibge_grupo_por_divisao(self, divisao):
        """Retorna todos os grupos de uma divisão\nParâmetros:\n- divisao: Código da divisão"""
        return requests.get(f"{self.ibge_grupo_por_divisao.format(divisao=divisao)}").json()

    def get_ibge_classe(self):
        """Retorna todas as classes do IBGE"""
        return requests.get(self.ibge_classe).json()
    
    def get_ibge_classe_por_identificador(self, identificador):
        """Retorna uma classe do IBGE por um identificador\nParâmetros:\n- identificador: Identificador da classe"""
        return requests.get(f"{self.ibge_classe_por_identificador}{identificador}").json()
    
    def get_ibge_classe_por_grupo(self, grupo):
        """Retorna todas as classes de um grupo\nParâmetros:\n- grupo: Código do grupo"""
        return requests.get(f"{self.ibge_classe_por_grupo.format(grupo=grupo)}").json()

    def get_ibge_subclasse(self):
        """Retorna todas as subclasses do IBGE"""
        return requests.get(self.ibge_subclasse).json()
    
    def get_ibge_subclasse_por_identificador(self, identificador):
        """Retorna uma subclasse do IBGE por um identificador\nParâmetros:\n- identificador: Identificador da subclasse"""
        return requests.get(f"{self.ibge_subclasse_por_identificador}{identificador}").json()
    
    def get_ibge_subclasse_por_classe(self, classe):
        """Retorna todas as subclasses de uma classe\nParâmetros:\n- classe: Código da classe"""
        return requests.get(f"{self.ibge_subclasse_por_classe.format(classe=classe)}").json()

    def get_api_secao(self):
        """Retorna todas as seções da API"""
        return requests.get(self.api_secao).json()

    def post_api_secao(self, codigo_secao, descricao_secao):
        """Insere uma seção na API\nParâmetros:\n- codigo_secao: Código da seção\n- descricao_secao: Descrição da seção"""
        formatted_data = {
            'cd_secao': codigo_secao,
            'de_secao': descricao_secao,
        }

        response = requests.post(self.api_secao, formatted_data)
        return f"{response.status_code} - {response.text}"     

    def get_api_divisao(self):
        """Retorna todas as divisões da API"""
        return requests.get(self.api_divisao).json()
    
    def post_api_divisao(self, codigo_divisao, descricao_divisao, id_secao):
        """Insere uma divisão na API\nParâmetros:\n- codigo_divisao: Código da divisão\n- descricao_divisao: Descrição da divisão\n- id_secao: Identificador da seção"""
        formatted_data = {
            'cd_divisao': codigo_divisao,
            'de_divisao': descricao_divisao,
            'id_secao': id_secao,
        }

        response = requests.post(self.api_divisao, formatted_data)
        return f"{response.status_code} - {response.text}"
    
    def get_api_grupo(self):
        """Retorna todos os grupos da API"""
        return requests.get(self.api_grupo).json()

    def post_api_grupo(self, codigo_grupo, descricao_grupo, id_divisao):
        """Insere um grupo na API\nParâmetros:\n- codigo_grupo: Código do grupo\n- descricao_grupo: Descrição do grupo\n- id_divisao: Identificador da divisão"""
        formatted_data = {
            'cd_grupo': codigo_grupo,
            'de_grupo': descricao_grupo,
            'id_divisao': id_divisao,
        }

        response = requests.post(self.api_grupo, formatted_data)
        return f"{response.status_code} - {response.text}"
    
    def get_api_classe(self):
        """Retorna todas as classes da API"""
        return requests.get(self.api_classe).json()

    def post_api_classe(self, codigo_classe, descricao_classe, id_grupo):
        """Insere uma classe na API\nParâmetros:\n- codigo_classe: Código da classe\n- descricao_classe: Descrição da classe\n- id_grupo: Identificador do grupo"""
        formatted_data = {
            'cd_classe': codigo_classe,
            'de_classe': descricao_classe,
            'id_grupo': id_grupo,
        }
        response = requests.post(self.api_classe, formatted_data)
        return f"{response.status_code} - {response.text}"            
    
    def get_api_subclasse(self, codigo_subclasse=''):
        """Retorna todas as subclasses da API"""
        return requests.get(f"{self.api_subclasse}{codigo_subclasse}").json()

    def post_api_subclasse(self, codigo_subclasse, descricao_subclasse, id_classe):
        """Insere uma subclasse na API\nParâmetros:\n- codigo_subclasse: Código da subclasse\n- descricao_subclasse: Descrição da subclasse\n- id_classe: Identificador da classe"""
        formatted_data = {
            'cd_subclasse': codigo_subclasse,
            'de_subclasse': descricao_subclasse,
            'id_classe': id_classe,
        }

        response = requests.post(self.api_subclasse, formatted_data)
        return f"{response.status_code} - {response.text}\nCódigo: {codigo_subclasse} - Descrição: {descricao_subclasse} - Classe: {id_classe}"

    def add_data(self):
        """Método para inserir os dados no banco de dados da API"""
        ## Inserir seções no banco de dados
        for secao in self.get_ibge_secao():
            print(self.post_api_secao(secao['id'], secao['descricao'].capitalize()))

        ## Inserir diviões no banco de dados com base nas seções já existentes na API
        for secao in self.get_api_secao():
            for divisao in self.get_ibge_divisao_por_secao(secao['cd_secao']):
                print(self.post_api_divisao(divisao['id'], divisao['descricao'].capitalize(), secao['id_secao']))

        ## Inserir grupos no banco de dados com base nas divisões já existentes na API
        for divisao in self.get_api_divisao():
            for grupo in self.get_ibge_grupo_por_divisao(divisao['cd_divisao']):
                print(self.post_api_grupo(grupo['id'], grupo['descricao'].capitalize(), divisao['id_divisao']))

        ## Inserir classes no banco de dados com base nos grupos já existentes na API
        for grupo in self.get_api_grupo():
            for classe in self.get_ibge_classe_por_grupo(grupo['cd_grupo']):
                print(self.post_api_classe(classe['id'], classe['descricao'].capitalize(), grupo['id_grupo']))

        ## Inserir subclasses no banco de dados com base nas classes já existentes na API
        for classe in self.get_api_classe():
            for subclasse in self.get_ibge_subclasse_por_classe(classe['cd_classe']):
                print(self.post_api_subclasse(subclasse['id'], subclasse['descricao'].capitalize(), classe['id_classe']))

        print('Finalizado')

    def main(self):
        mes = {
            'JANEIRO': 1,
           'FEVEREIRO': 2,
            'MARÇO': 3,
            'ABRIL': 4,
            'MAIO': 5,
            'JUNHO': 6,
            'JULHO': 7,
            'AGOSTO': 8,
            'SETEMBRO': 9,
            'OUTUBRO': 10,
            'NOVEMBRO': 11,
            'DEZEMBRO': 12
               }

        divisao_setor = {
            'PRIMÁRIO': 1,
            'SECUNDÁRIO': 2,
            'TERCIÁRIO': 3
        }

        setor_economico = {
            'COMÉRCIO': 1,
            'SERVIÇO': 2,
            'MEIO AMBIENTE - SERVIÇO': 3,
            'INDUSTRIA': 4,
            'AGROPECUÁRIA E PESCA': 5
        }

        for index, row in self.dataframe.iterrows():

            cd_subclasse = str(row['CD_SUBCLASSE'])
            if len(cd_subclasse) == 6:
                cd_subclasse = f"0{cd_subclasse}"
                
            response = requests.get(f"{self.api_subclasse}{cd_subclasse}")
            cd_subclasse = response.json()['id_subclasse']

            data = {
                "vl_arrecadacao": float(row['VL_PGTO']),
                "id_divisao_setor": divisao_setor[row['DE_DIVISAO_SETOR']],
                "id_setor_economico": setor_economico[row['DE_SETOR_ECONOMICO']],
                "id_data": mes[row['DE_MES_COMP']],
                "id_subclasse": cd_subclasse
            }    
            try: 
                response = requests.post(self.api_arrecadacao, data)
                print(f"{response.status_code} - {response.text}")
                
            except Exception as e:
                print(e)

if __name__ == '__main__':
    Request('spreadsheets/setor_economico_ajustado2.xlsx').main()

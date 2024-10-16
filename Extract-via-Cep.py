import requests
import pymssql
from assets.utils import insert_banco

def buscar_cep(cep):
    
    # API ViaCEP
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    
    # Verifica a requisição
    if resposta.status_code == 200:
        dados = resposta.json()
        if 'erro' not in dados:
            return dados
        else:
            return None
    else:
        return None

def main():
    lista_de_cep = ['','','']
    for cep in lista_de_cep:
        dados_cep = buscar_cep(cep)
        if dados_cep:
            insert_banco(dados_cep)
        else:
            pass

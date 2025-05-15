#usando funções:

import requests
from tinydb import TinyDB
from datetime import datetime
import time

def extrair():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url) #Como se estivesse fazendo requisição ao BD
    return response.json()

def transformar(dados_json):
    valor = (dados_json['data']['amount'])
    criptomoeda = dados_json['data']['base']
    moeda = dados_json['data']['currency']
    dados_tratados = {
        "valor": valor,
        "criptomoeda": criptomoeda,
        "moeda": moeda,
        "timestamp": datetime.now().isoformat()
                }
    return dados_tratados

def load(dados_tratados):
    db = TinyDB('db.json') #importando Banco de Dados
    db.insert(dados_tratados) #inserindo os dados tratados no BD
    print("Dados salvos com sucesso") #Não tem return porque é só para salvar os dados


if __name__ == "__main__":
    while True:
        dados_json = extrair()
        dados_tratados = transformar(dados_json)
        load(dados_tratados)
        time.sleep(5)
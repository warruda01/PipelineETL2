import requests

url = "https://api.coinbase.com/v2/prices/spot"

response = requests.get(url) #Como se estivesse fazendo requisição ao BD

print(response.json())



import requests

url = 'https://economia.awesomeapi.com.br/all/USD-BRL'

response = requests.get(url)

if response.status_code == 200:
    dolar_value = response.json()['USD']['low']
    print(f'O valor do Dólar é R${dolar_value}')
else:
    print('Erro ao buscar valor do Dólar!')
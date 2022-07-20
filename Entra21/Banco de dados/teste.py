import Funções_Mercado
import requests


cep = input('Informe seu CEP')
alvo = f'https://viacep.com.br/ws/{cep}/json/'
response = requests.get(alvo)
rcep = response.json()
rua = rcep['logradouro']
bairro = rcep['bairro']
localidade = rcep['localidade']
uf = rcep['uf']




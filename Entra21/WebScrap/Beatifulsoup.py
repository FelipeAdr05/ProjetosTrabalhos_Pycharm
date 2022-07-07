import requests
from bs4 import BeautifulSoup
from operator import itemgetter

produtos = []
valores = []
geral = []

for i in range(2):
    url = f'https://www.samsclub.com.br/limpeza?p={i}'
    response = requests.get(url)
    html = BeautifulSoup(response.text, 'html.parser')

    for produto in html.select('.vtex-product-summary-2-x-brandName'):
        produtos.append(produto.text.strip())

    for valor in html.select('.vtex-productShowCasePrice'):
        valores.append(float(valor.text.strip().replace('R$ ', '').replace(',', '.')))


for i in range(len(produtos)):
    dic = {'Produto': produtos[i], 'Valor': valores[i]}
    geral.append(dic)


geral_novo = sorted(geral, key=itemgetter('Valor'))

for i in geral_novo:
    print(i)




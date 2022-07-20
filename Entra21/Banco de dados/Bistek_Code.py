import requests
from bs4 import BeautifulSoup
import sqlite3
import arrow

ar = arrow.now().format('DD/MM/YYYY')

conexao = sqlite3.connect('teste do scrapy.db')
cursor = conexao.cursor()

# produtos = []
# valores = []
# for i in range(60):
#     alvo = f'https://www.bistek.com.br/bebidas/vinhos-e-espumantes.html?p={i}'
#     response = requests.get(alvo)
#     html = BeautifulSoup(response.text, 'html.parser')
#
#     for produto in html.select('.product-item-link'):
#         produtos.append(produto.text.strip())
#
#     for valor in html.select('.price-wrapper .price'):
#         valores.append(float(valor.text.strip().replace('R$ ','').replace(',', '.')))
#
# for i in range(len(produtos)):
#     cursor.execute('INSERT INTO dados(data, produto, valor) '
#                    'VALUES(?,?,?)', (ar, produtos[i], valores[i]))
#     conexao.commit()

valor = 150
cursor.execute(f'SELECT * FROM dados WHERE valor > {valor}')
for linha in cursor.fetchall():
    print(f'{linha[0]} - {linha[1]} - {linha[2]} - R$ {linha[3]:.2f}')

cursor.close()
conexao.close()


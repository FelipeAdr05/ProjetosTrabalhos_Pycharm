import sqlite3
import requests

conexao = sqlite3.connect('mercadobanco.db')
cursor = conexao.cursor()

lista_clientes = []
listacep = []
info_nome = input('Digite seu nome: ')
info_cpf = input('Digite seu CPF: ').replace('.', '').replace('-','')
info_cep = input('Digite seu CEP: ')
info_numero = input('Digite seu número: ')
lista_clientes.append(info_nome)
lista_clientes.append(info_cpf)
lista_clientes.append(info_numero)
alvo = f'https://viacep.com.br/ws/{info_cep}/json/'
response = requests.get(alvo)
rcep = response.json()
dict.pop(rcep, 'ibge')
dict.pop(rcep, 'ddd')
dict.pop(rcep, 'gia')
dict.pop(rcep, 'siafi')
dict.pop(rcep, 'complemento')

for i in rcep:
    listacep.append(rcep[i])



cursor.execute('INSERT INTO Clientes(nome_cliente, CPF_cliente, CEP, numero)'
               f'VALUES("{lista_clientes[0]}","{lista_clientes[1]}", "{listacep}", "{lista_clientes[2]}")')


conexao.commit()


conexao.close()


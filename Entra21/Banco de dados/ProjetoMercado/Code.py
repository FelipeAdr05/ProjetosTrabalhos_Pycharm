import sqlite3
import requests

class Cliente:
    def __init__(self, nome, cpf, cep, numero):
        self.nome = nome
        self.cpf = cpf
        self.cep = cep
        self.numero = numero

class Produtos:
    def __init__(self, nome, familia, cod_barra):
        self.nome = nome
        self.familia = familia
        self.cod_barra = cod_barra

class Vendas:
    def __init__(self, data, cod_barras, cpf, quantidade, valor_unitario, valor_total):
        self.data = data
        self.cod_barras = cod_barras
        self.cpf = cpf
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.valor_total = valor_total


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


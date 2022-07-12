import sqlite3
import requests
import Funções_Mercado as fm

print('''Olá, informe oque deseja fazer
[1] Já tem cadastro?
[2] Deseja se cadastrar?
[3] Sair
''')
op = input('>>> ')
if op == '1':
    pass
elif op == '2':
    lista_cliente = fm.cadastro()
    print(lista_cliente)
else:
     quit()

conexao = sqlite3.connect('mercado.db')
cursor = conexao.cursor()


cursor.execute('INSERT INTO Clientes (Nome_cliente, CPF_cliente, CEP, Número)'
               f'VALUES ("{lista_cliente[0]}", "{lista_cliente[1]}", "{lista_cliente[2]}", "{lista_cliente[3]}")')


conexao.commit()






cursor.close()
conexao.close()
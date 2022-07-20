# CRUD
# Create - Create
# Read - Select
# Update - Update
# Delete - Delete/Drop

import sqlite3

conexao = sqlite3.connect('basededados.db')
cursor = conexao.cursor()

cursor.execute('DROP TABLE frutas')

# CRUD
# Create

# cursor.execute('CREATE TABLE IF NOT EXISTS frutas ('
#                'id INTEGER PRIMARY KEY AUTOINCREMENT,'
#                'nome_fruta TEXT,'
#                'tipo TEXT)')
# conexao.commit()

# cursor.execute('INSERT INTO frutas(nome_fruta, tipo)'
#                'VALUES("maça","verde")')
# conexao.commit()

# cursor.execute('SELECT * FROM frutas')
# for linha in cursor.fetchall():
#     print(f'{linha[0]} - {linha[1]} - {linha[2]}')
#
# cursor.execute('UPDATE frutas SET nome_fruta="Banana" WHERE id=1')
#
# conexao.commit()

# jamais farás UPDATE sem WHERE

# print(30*'=-')

# cursor.execute('SELECT * FROM frutas WHERE nome_fruta ="Banana"')
# for linha in cursor.fetchall():
#     print(f'{linha[0]} - {linha[1]} - {linha[2]}')

# cursor.execute('DELETE FROM frutas WHERE id=2')
# conexao.commit()
#
# cursor.execute('SELECT * FROM frutas WHERE nome_fruta ="Banana"')
# for linha in cursor.fetchall():
#     print(f'{linha[0]} - {linha[1]} - {linha[2]}')


cursor.close()
conexao.close()

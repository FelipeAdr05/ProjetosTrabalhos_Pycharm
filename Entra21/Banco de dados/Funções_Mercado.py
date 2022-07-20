import requests

def cadastro():
    lista_cliente = []
    nome = input('Informe seu nome completo: ').upper()
    cpf = input('Informe o seu CPF: ').replace('.', '').replace('-', '')
    cep = input('Informe o seu CEP: ').replace('-', '')
    alvo = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(alvo)
    rcep = response.json()
    dict.pop(rcep, 'ibge')
    dict.pop(rcep, 'ddd')
    dict.pop(rcep, 'gia')
    dict.pop(rcep, 'siafi')
    dict.pop(rcep, 'complemento')
    numero_casa = input('Informe o número de sua casa: ')
    lista_cliente.append(nome)
    lista_cliente.append(cpf)
    lista_cliente.append(cep)
    lista_cliente.append(numero_casa)
    print(lista_cliente)







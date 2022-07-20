# Função map aplica uma função em cada item da lista de itens

precos = [1000, 1500, 1250, 2500]

# quero conferir o preço com imposto de cada item da minha lista
def adicionar_imposto(preco):
    return preco * 1.1

# usando for
precos_com_imposto = []
for preco in precos
    precos_com_imposto.append(adicionar_imposto(preco))
print(precos_com_imposto)
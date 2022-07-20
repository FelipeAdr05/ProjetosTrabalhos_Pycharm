from abc import ABC, abstractmethod
import random
from time import sleep


class Supermercado(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def vender(self):
        return True


class Produtos(Supermercado):
    def __init__(self, nome, preco, categoria, peso, validade):
        super().__init__(nome)
        self.categoria = categoria
        self.peso = peso
        self.validade = validade
        self.preco = preco

    def checagem(self):
        print(f'''Nome: {self.nome}
Preço: R${self.preco}
Categoria: {self.categoria}
Peso: {self.peso}
Validade: {self.validade}''')

    def vender(self):
        print('Pip... Produto vendido!')

    def guardar(self):
        print('Guardando Produto...')


class Caixa(Supermercado):
    def __init__(self, nome, fila):
        super().__init__(nome)
        self.fila = False

    def vender(self):
        return True

    def bipar(self):
        print('Passando Produtos...')
        sleep(1.4)

    def metodo(self):
        r = input('Qual o método de pagamento?\n[1] Débito\n[2] Crédito\n>>> ')
        if r == '1':
            print('Passando compra em Débito...')
        else:
            print('Passando compra em Crédito...')

    def aprovado(self):
        while True:
            x = input('Pagar? Pressione aqui [X] para pagar\nPressione aqui [Z] para cancelar\n>>> ').upper()
            if x == 'X':
                r = random.randint(1, 4)
                if r != 1:
                    print('Pagamento Aprovado')
                    break
                else:
                    print('Erro na maquininha, tente novamente')
                    sleep(1.5)
                    continue
            else:
                break

fila = random.randint(1,3)
caixa = Caixa('Marcela', fila)


def main():
    while True:
        dic = {}
        print('''----------MERCADO----------''')
        nome_usuario = input('Olá, qual seu nome?\n>>> ')
        n = input('Qual o nome do produto?\n>>> ')
        pr = input('Qual o preço do produto?\n>>> R$ ')
        c = input('Qual a categoria do produto?\n>>> ')
        p = input('Qual o peso do produto?\n>>> ')
        v = input('Qual a validade do produto?\n>>> ')
        objeto = Produtos(n, pr, c, p, v)
        dic.update({"produto": "caracteristicas"})
        r = input('Deseja escolher mais um produto? [S] ou [N]\n>>> ').upper()
        if r == 'S':
            continue
        elif r == 'N':
            sleep(1)
            print('Indo até o caixa')
            if fila == 1:
                print('Voce pegou fila... Aguarde')
                sleep(random.randint(3, 6))
                print('Pronto!')
                sleep(0.4)
            else:
                print('Ufa.. Não tinha fila')
            break
    sleep(0.8)
    print(f'Olá {nome_usuario}!!')
    sleep(0.8)
    print('Bom dia')
    sleep(1.1)
    caixa.bipar()
    sleep(0.8)
    caixa.metodo()
    sleep(0.8)
    caixa.aprovado()

main()

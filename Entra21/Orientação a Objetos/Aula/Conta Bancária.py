class Conta:
    def __init__(self, conta, nome, saldo=0.0):
        self.conta = conta
        self.nome = nome
        self.__saldo = saldo

    def ver_saldo(self):
        print(f'Seu saldo é R${self.__saldo}')
        self.__falarnome()

    def __falarnome(self):
        print(f'Bom dia, {self.nome}')


c1 = Conta(123456, 'Felipe', 100)
c1.ver_saldo()
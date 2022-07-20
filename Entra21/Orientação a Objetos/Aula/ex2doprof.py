class Lata:
    def __init__(self, altura, diametro, cor, peso, material, volume):
        self.altura = altura
        self.diametro = diametro
        self.cor = cor
        self.peso = peso
        self.material = material
        self.volume = volume
        self.aberta = False
        self.amassada = False
        self.descartada = False
        self.lacre = True

    def abrir(self):
        if self.aberta:
            print('Ja está aberta!')
        else:
            print('POC')
            self.aberta = True

    def beber(self, quantidade):
        if not self.aberta:
            print(f'A lata está fechada')
        elif self.descartada:
            print('Lata ja foi descartada')
        elif self.volume == 0:
            print('A lata esta vazia ')
        elif self.aberta >= quantidade:
            self.volume -= quantidade
            print(f'Ainda restam {self.volume}ml')
        elif quantidade > self.volume:
            print(f'Voce bebeu {self.volume} e faltou {-(self.volume-quantidade)} ml')
            self.volume = 0

    def esvaziar(self):
        if not self.aberta:
            print('Esta fechada')
        elif self.volume == 0:
            print('A lata ja esta vazia')
        elif self.descartada:
            print('A lata a nem existe mais')
        elif self.amassada:
            print('A lata ja foi amassada')
        else:
            self.volume = 0
            print('A lata está vazia')

    def amassar(self):
        if self.amassada:
            print('A lata ja foi amassada')
        elif self.descartada:
            print('A lata ja esta descartada')
        elif self.volume == 0:
            print('A lata foi amassada')
            self.amassada = True
        else:
            print('Voce precisa beber tudo antes de amassar')

    def tirar_lacre(self):
        if self.descartada:
            print('A lata ja foi descartada')
        elif not self.lacre:
            print('Voce ja tirou o lacre')
        else:
            print('Voce removeu o lacre')
            self.lacre = False

    def descartar(self, cor_do_lixo):
        if self.descartada:
            print('Ja foi descartada')
        elif not self.amassada:
            print('Só pode descartar depois de amassar')
        elif cor_do_lixo != 'AMARELO':
            print('Nao pode ser descartado nessa lixeira!')
        else:
            print('Lata descartada no local correto!')
            self.descartada = True





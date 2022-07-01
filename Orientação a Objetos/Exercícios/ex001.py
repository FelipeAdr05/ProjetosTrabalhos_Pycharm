class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocacor(self, cor):
        while True:
            print(f'A cor da bola é {cor}')
            r = input(' Deseja mudar a cor da bola? [S] ou [N]\n>>> ').upper()
            if r == 'S':
                cor = input('Qual cor você quer? ')
            else:
                break


bola = Bola('Branca', 700, 'couro sintético')

bola.trocacor(cor='Branca')


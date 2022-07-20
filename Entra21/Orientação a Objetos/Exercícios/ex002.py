class Quadrado:
    def __init__(self, tamanhodolado):
        self.tamanhodolado = tamanhodolado

    def mudarvalor(self, novo_tamanho):
            print(f'O tamanho do quadrado era: {self.tamanhodolado}cm, e virou {novo_tamanho}cm')
            self.tamanhodolado = int(novo_tamanho)

    def calcular(self):
        area = self.tamanhodolado**2
        print(f'A área do quadrado é {area}cm²')

quadrado = Quadrado(10)

while True:
    print(f'O tamanho do quadrado é {quadrado.tamanhodolado}cm')
    quadrado.mudarvalor(novo_tamanho=input('Qual o novo tamanho desejado? '))
    r = input(f'Deseja calcular a área deste quadrado? ').upper()
    if r == 'S':
        quadrado.calcular()
    else:
        break



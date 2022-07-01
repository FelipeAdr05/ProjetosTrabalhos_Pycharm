# Criar uma classe para uma latinha de coca-cola.
# a classe deve ter todos os atributos dimensionais
# e suas caracteristicas de material
# as funcionabilidades(métodos) da garrafa sao, abrir,
# beber, esvaziar, amassar, retirar lacre e descartar

from time import sleep

class LatadeCoca:
    def __init__(self, altura, diametro, material):
        self.altura = altura
        self.diametro = diametro
        self.material = material

    def abrir(self):
        print('Abrindo sua lata de \033[1;31mCoca-Cola\033[1;0m')

    def beber(self):
        print('Bebendo sua lata de \033[1;31mCoca-Cola\033[1;0m')

    def esvaziar(self):
        print('Sua lata esta vazia')

    def amassar(self):
        print('Amassando lata de \033[1;31mCoca-Cola\033[1;0m')

    def retirar_lacre(self):
        print('Retirando lacre da lata')

    def descartar(self):
        print('Descartando Lata de \033[1;31mCoca-Cola\033[1;0m')

lata = LatadeCoca('144mm', '52mm', 'Alumínio')


print(f'A lata tem {lata.altura} de altura, {lata.diametro} de diametro e é feita de {lata.material}')
print('=-'*30)
sleep(1.5)
lata.abrir()
sleep(1.5)
lata.beber()
sleep(1.5)
lata.esvaziar()
sleep(1.5)
lata.amassar()
sleep(1.5)
lata.retirar_lacre()
sleep(1.5)
lata.descartar()
sleep(1.5)

# criar uma classe chamada de veiculos,
# onde tenho pelo menos 5 atributos.
# tambem devem ser criados 5 objetos
# Classe, onde cada item deve ser cadastrato via Input



class Carro:
    def __init__(self, modelo, tipo, motor, lugares, portas):
        self.modelo = modelo
        self.tipo = tipo
        self.motor = motor
        self.lugares = lugares
        self.portas = portas

def __repr__(self):
    return repr(f' {self.modelo} {self.tipo} {self.motor} {self.lugares} {self.portas}')


def ligar():
    print('Wrum Wrum')

def desligar():
    print('Zzzzz')


cadastros = []
for i in range(2):
    modelo = input('Digite o modelo: ')
    tipo = input('Digite o tipo: ')
    motor = input('Digite o motor: ')
    lugares = input('Digite a quantidade de lugares: ')
    portas = input('Digite a quantidade de portas: ')
    caracteristicas = Carro(modelo, tipo, motor, lugares, portas)
    cadastros.append(caracteristicas.__dict__)

print(cadastros)






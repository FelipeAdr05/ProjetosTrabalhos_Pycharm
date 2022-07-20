from time import sleep

class Console:
    def __init__(self, controle, armazenamento, midia, marca, cor='Preto'):
        self.controle = controle
        self.armazenamento = armazenamento
        self.midia = midia
        self.marca = marca
        self.cor = cor

    def ligar(self):
        print(f'Ligando {self.marca}')
        sleep(1)
        print("Turuunn")

    def desligar(self):
        print(f'Desligando {self.marca}')
        sleep(1)
        print("Tuduunn")

class Playstation(Console):
    def __init__(self, controle, armazenamento, midia, marca='Playstation'):
        super().__init__(controle, armazenamento, midia, marca)


    def bugar(self):
        print('Bugou')

v1 = Console(2, 'HD', 'Física', 'Nintendo', 'Azul')
v2 = Playstation(1, 'SSD', 'Digital')

v2.bugar()
from time import sleep


class Carro:
    def __init__(self, nome, consumo, qnt_tanque=0.0):
        self.nome = nome
        self.consumo = consumo
        self.qnt_tanque = qnt_tanque

    def abastercer(self):
        r = float(input('Quanto você deseja abastecer?\n>>> '))
        self.qnt_tanque += r

    def verificar(self):
        print(f'Você tem {self.qnt_tanque}L de gasolina')

    def andar(self):
        if self.qnt_tanque == 0:
            sleep(0.8)
            print('Ops... Sem combustível, abasteça!')
            return self.abastercer()
        else:
            dist = float(input('Quanto quilômetros você quer andar?\n>>> '))
            gasto = dist / self.consumo
            if gasto > self.qnt_tanque:
                dis_percorrida = self.consumo * self.qnt_tanque
                print(f'Seu tanque zerou!! Abasteça!')
                print(f'a distância percorrida até o momento é de {dis_percorrida}Km')
                self.qnt_tanque = 0
                c_trajeto = (dist - dis_percorrida) / self.consumo
                print(f'Ainda falta {dist - dis_percorrida}Km para terminar o trajeto você precisa abasatecer {c_trajeto:.2f}L')
            else:
                print(f'Você andou {dist}Km e consumiu {gasto:.2f}L de gasolina.')
                self.qnt_tanque -= gasto

def main():
    nome_carro = input('Qual o nome do carro: ')
    gas = float(input('Qual o consumo do carro? (Km/l) '))
    tank = float(input('Quanto de combustivel tem? '))
    carro1 = Carro(nome_carro, gas, tank)

    while True:

        print('''--------------Menu--------------
[1] Andar   
[2] Abastecer                           
[3] Verificar nível de gasolina      
[4] Sair                             
''')
        op = input('>>> ')
        if op == '1':
            carro1.andar()
        elif op == '2':
            carro1.abastercer()
        elif op == '3':
            carro1.verificar()
        elif op == '4':
            break

main()





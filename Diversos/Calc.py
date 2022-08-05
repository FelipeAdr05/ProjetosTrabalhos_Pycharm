from random import randint

print("=-"*40)
print('Calculadora Virtual')
print("=-"*40)
while True:
    operacao = input('''
[+] - 1
[-] - 2
[*] - 3
[/] - 4

>>> ''')

    valor1 = float(input('Digite o 1º número: '))
    valor2 = float(input('Digite o 2º número: '))

    if operacao == '1':
        resultado = valor1 + valor2
    elif operacao == '2':
        resultado = valor1 - valor2
    elif operacao == '3':
        resultado = valor1 * valor2
    else:
        resultado = valor1 / valor2

    print(resultado)
    r = input('Deseja usar novamente? [S] ou [N]\n>>> ').upper()
    if r == 'N':
        break








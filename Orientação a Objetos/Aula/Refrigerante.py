from ex2doprof import Lata
from time import sleep

latinha = Lata('144mm', '52mm', 'Vermelha', '14g', 'Alumínio', 350)


latinha.abrir()
sleep(1.5)
latinha.beber(quantidade=int(input('Qual a quantidade?')))
sleep(1.5)
latinha.esvaziar()
sleep(1.5)
latinha.tirar_lacre()
sleep(1.5)
latinha.amassar()
sleep(1.5)
latinha.descartar(cor_do_lixo=input('Qual a cor do lixo? ').upper())
sleep(1.5)


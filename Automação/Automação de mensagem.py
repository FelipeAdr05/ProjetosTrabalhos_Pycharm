import pyautogui as pi
from time import sleep

cont = -25
while True:
    sleep(1)
    pi.click(323, 97)  # botao de contatos
    sleep(0.1)
    pi.moveTo(290, 342)  # coloca o cursor para deslizar
    sleep(0.1)
    pi.scroll(cont)  # desliza para o proximo contato
    cont -= 25
    sleep(0.1)
    pi.click(290, 342) # clica no contato
    sleep(0.1)
    pi.click(660, 648)  # clicar no botao de chat
    sleep(0.1)
    pi.hotkey('ctrl', 'v')  # cola a mensagem escolhida
    sleep(0.1)
    # pi.press('enter') # envia a mensagem
    sleep(0.1)
    pi.click(23, 150)
    sleep(0.1)
    pi.click(261, 213) # clica no CA
    sleep(0.1)
    pi.click(660, 648)  # clicar no botao de chat
    sleep(0.1)
    pi.hotkey('ctrl', 'v')  # cola a mensagem escolhida
    sleep(0.1)
    pi.press('enter') # envia a mensagem para o CA
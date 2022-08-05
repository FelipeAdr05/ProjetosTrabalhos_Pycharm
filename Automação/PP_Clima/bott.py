import os
import time
import re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from collections import Counter as cnt
from selenium.webdriver.common.by import By
from time import sleep


class Newbot:
    def __init__(self, nome_bot):
        self.driver = webdriver.Chrome()

    def climaTempo(self):
        site = 'https://www.climatempo.com.br/previsao-do-tempo/cidade/372/blumenau-sc'
        self.driver.get(site)
        self.driver.implicitly_wait(5)
        temp_min = self.driver.find_element(By.XPATH, '//*[@id="min-temp-1"]').text
        temp_max = self.driver.find_element(By.XPATH, '//*[@id="max-temp-1"]').text
        dat1 = datetime.now().strftime("%H:%M")
        dat2 = datetime.now().strftime("%d/%m")
#        print(f'''Previsão de Hoje {dat2} Blumenau - SC
# Horário: {dat1}
        
# Temperatura Mínima: {temp_min}C
# Temperatura Máxima: {temp_max}C
# ''')


class Cell:
    def __init__(self, nome):
        self.driver = webdriver.Chrome()

    def mensagem(self):
        email = input('Digite seu email: ')
        senha = input(' Digite sua senha: ')
        site = 'https://login.live.com/'
        self.driver.get(site)
        self.driver.find_element(By.XPATH, '//*[@id="i0116"]').send_keys(email)
        self.driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
        sleep(0.8)
        self.driver.find_element(By.XPATH, '//*[@id="i0118"]').send_keys(senha)
        self.driver.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="idBtn_Back"]').click()
        self.driver.implicitly_wait(4)
        self.driver.find_element(By.XPATH, '//*[@id="home.cards.card.outlook.cold"]/div[2]/div').click()
        self.driver.implicitly_wait(4)
        self.driver.find_element(By.XPATH, '//*[@id="app"]/div/div[2]/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/div/div/button/span').click()







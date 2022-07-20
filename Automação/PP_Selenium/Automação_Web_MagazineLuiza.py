from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from time import sleep

navegador = wd.Chrome()
navegador.get("https://ri.magazineluiza.com.br/")
navegador.find_element(By.XPATH, '//*[@id="Form1"]/header/div/div/div/div[1]/button').click()
sleep(0.7)
navegador.find_element(By.XPATH, '//*[@id="heading-mobile-3"]/button').click()
sleep(0.3)
navegador.find_element(By.XPATH, '//*[@id="Form1"]/div[6]/a').click()
sleep(0.3)
navegador.find_element(By.XPATH, '//*[@id="collapse-mobile-3"]/div/ul/li[2]/a').click()
sleep(1)
navegador.find_element(By.XPATH, '//*[@id="52UstABBxF8k7Q9IXxA3iw=="]').click()

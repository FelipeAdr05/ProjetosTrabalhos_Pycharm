from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
navegador = webdriver.Chrome()

navegador.get("https://login.live.com/")
navegador.find_element(By.XPATH, '//*[@id="i0116"]').send_keys("email")
navegador.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
sleep(0.8)
navegador.find_element(By.XPATH, '//*[@id="i0118"]').send_keys("senha")
navegador.find_element(By.XPATH, '//*[@id="idSIButton9"]').click()
navegador.find_element(By.XPATH, '//*[@id="idBtn_Back"]').click()

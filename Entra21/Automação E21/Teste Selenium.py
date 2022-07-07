from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
from time import sleep

email = 'felipeadrnunes@gmail.com'
senha = '05102004'

navegador = webdriver.Chrome()
navegador.get('https://externo.proway.com.br/login-aluno')

# navegador.find_element(By.XPATH, '//*[@id="formLoginSubscriber_username"]').send_keys(email)
# navegador.find_element(By.XPATH, '//*[@id="formLoginSubscriber_password"]').send_keys(senha)
# navegador.find_element(By.XPATH, '//*[@id="formLoginSubscriber"]/div[3]/div/div/div/button').click()

navegador.find_element('xpath', '//*[@id="formLoginSubscriber_username"]').send_keys(email)
navegador.find_element('xpath', '//*[@id="formLoginSubscriber_password"]').send_keys(senha)
sleep(1)
navegador.find_element('xpath', '//*[@id="formLoginSubscriber"]/div[3]/div/div/div/button').click()
sleep(1)
navegador.find_element('xpath', '//*[@id="root"]/section/section/main/div/div/div/ul/li[1]/ul/li/button').click()
sleep(1)
navegador.find_element('xpath', '//*[@id="dailyEvaluationForm_hoje"]/div/label[5]').click()
navegador.find_element('xpath', '//*[@id="dailyEvaluationForm_instrutorMetodologia"]/div/label[5]').click()
navegador.find_element('xpath', '//*[@id="dailyEvaluationForm_instrutorPostura"]/div/label[5]').click()
navegador.find_element('xpath', '//*[@id="dailyEvaluationForm_instrutorDominio"]/div/label[5]').click()
navegador.find_element('xpath', '//*[@id="dailyEvaluationForm_empresaAmbiente"]/div/label[5]').click()
navegador.find_element('xpath', '//*[@id="dailyEvaluationForm_empresaMicro"]/div/label[5]').click()
navegador.find_element('xpath', '//*[@id="dailyEvaluationForm_empresaRecepcao"]/div/label[5]').click()
sleep(1)
navegador.find_element('xpath', '/html/body/div[3]/div/div[2]/div/div[2]/div[3]/button[2]').click()
sleep(1)
navegador.quit()

import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Para executar em ambiente linux é necessario instalar o Firefox fora do SNAP
drive = webdriver.Firefox()

drive.get('file:///home/zenxbr/PycharmProjects/PythonProject/treiner/automacao-web/alert.html')
time.sleep(1)
position = drive.find_element(By.NAME, "alerta1")
time.sleep(2)
position.click()
objeto = drive.switch_to.alert
mensagem = objeto.text
print('Mensagem de alerta: \n' + mensagem)
time.sleep(1)
objeto.accept()
print('Clicado na tela automaticamente')
drive.close()

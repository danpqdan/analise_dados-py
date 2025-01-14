import time

import pyautogui as py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

py.sleep(2)
html_code = '''<html>
<head>
<title>Teste Selenium</title>
</head>
<body bgcolor = "yellow">
<form>
<label>Nome</label><br>
<input type="text" name="nome" placeholder="Digite seu nome">
<p>
<label>Telefone</label><br>
<input type="text" name="telefone" placeholder="Digite seu telefone">
<p>
<label>E-Mail</label><br>
<input type="text" name="email" placeholder="Digite seu e-mail">
<p>
<label>Confirma seu dados?</label><br>
<input type="checkbox" name="confirma">
<p>
<br>
<input type="reset" value="Limpar" name = "limpar">
</form>
</body>
</html>'''
py.PAUSE = 2
py.press('win')
time.sleep(2)
py.write('gedit')
py.press('enter')
time.sleep(2)
py.write(html_code)
py.hotkey('ctrl', 's')
py.write('/home/zenxbr/PycharmProjects/PythonProject/treiner/automacao-web/input.html')
py.press(['enter', 'enter'], interval=1)
py.hotkey('alt', 'f4')

driver = webdriver.Firefox()
driver.get('file:///home/zenxbr/PycharmProjects/PythonProject/treiner/automacao-web/input.html')
time.sleep(3)
inputName = driver.find_element(By.NAME, 'nome')
inputName.send_keys("Daniel de Jesus S.")
inputTel = driver.find_element(By.NAME, 'telefone')
inputTel.send_keys('(11) 96269-6757')
inputEmail = driver.find_element(By.NAME, 'email')
inputEmail.send_keys('danieltisantos@gmail.com')
send = driver.find_element(By.NAME, 'confirma')
send.send_keys(Keys.SPACE)
time.sleep(3)
clear = driver.find_element(By.NAME, 'limpar')
clear.send_keys(Keys.RETURN)

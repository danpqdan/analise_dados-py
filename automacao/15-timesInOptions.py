import time

import pyautogui as py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

text_html = ('''<html>
<head>
<title>Teste Selenium</title>
</head>
<body bgcolor = "yellow">
<form>
<label>Selecione o seu time:</label><br>
<select name="time" id="time" class="time">
<option id="1" value="1">Palmeiras</option>
<option id="2" value="2">São Paulo</option>
<option id="3" value="3">Santos</option>
<option id="4" value="4">Corinthians</option>
</select>
<select name="confirmar" id="confirmar" class="confirmar">
<option id="1" value="1"></option>
<option id="2" value="2">Sim</option>
<option id="3" value="3">Nao</option>
</select>
</form>
</body>
</html>''')

py.press('win')
time.sleep(3)
py.write('gedit')
time.sleep(2)
py.press('enter')
py.sleep(2)
py.write(text_html)
py.hotkey('ctrl', 's')
py.write('/home/zenxbr/PycharmProjects/PythonProject/treiner/automacao-web/times.html')
py.press('enter', interval=3, presses=4)
py.hotkey('alt', 'f4')
time.sleep(2)
driver = webdriver.Firefox()
driver.get('file:///home/zenxbr/PycharmProjects/PythonProject/treiner/automacao-web/times.html')
time.sleep(2)
time = driver.find_element(By.ID, "time")
sel = Select(time)  # Classe responsavel para dropbox e menus Options
# sel.select_by_visible_text("Corinthians")
# sel.select_by_index(3)
sel.select_by_value("3")
confirm = driver.find_element(By.XPATH, '//*[@class="confirmar"]')
sel = Select(confirm)

sel.select_by_visible_text("Sim")
time.sleep(15)
driver.close()

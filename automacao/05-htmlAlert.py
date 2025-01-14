import time

import pyautogui as py
from selenium import webdriver

time.sleep(2)
html_code = '''<!DOCTYPE html>
<html>
  <body bgcolor="#C0C0C0">
    <h1>Demonstration of Alert</h1>
    <p>Click the button to create an alert</p>
    <button onclick="func_alerta()" name="alerta1">Create Alert</button>
    <script>
      function func_alerta() {
        alert("Hi!, I am a simple alert. Please click OK");
      }
    </script>
  </body>
</html>'''
py.PAUSE = 2
py.press('win')
time.sleep(1)
py.write('gedit')
py.press('enter')
py.write(html_code)
time.sleep(5)
py.hotkey('ctrl', 's')
py.write('/home/zenxbr/PycharmProjects/PythonProject/treiner/automacao-web/alert.html')
py.press('enter')
py.press('enter')
py.hotkey('alt', 'f4')
time.sleep(1)
drive = webdriver.Edge()
drive.get('file:///home/zenxbr/PycharmProjects/PythonProject/treiner/automacao-web/alert.html')
time.sleep(1)
locale = py.locateCenterOnScreen(
    '/home/zenxbr/PycharmProjects/PythonProject/treiner/automacao-web/btn_alert.png', confidence=0.5)
py.click(locale.x, locale.y, 1)
for i in range(0, 3):
    time.sleep(3)
    i += 1

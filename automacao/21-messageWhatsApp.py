import time

import pyautogui as py
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")
driver.implicitly_wait(36000)  # Segundos
texto = '''🌟 *Boa tarde a todos!* 🌟  
Foi questionado antes sobre o que estávamos achando da *Automatização de tarefas com PyAutoGui* e confesso que foi meu primeiro contato com _automação_ e até estava me perguntando para qual finalidade poderia me servir, já que poderia muito bem ir lá e fazer *na mão*...
      
Com muita inocência, esse questionamento durou pouco. O fato de conseguir interagir de forma rápida e eficaz com planilhas e editores de texto, sem nem ao menos abrir um *EXCEL* ou *WORD*, é realmente incrível.  

🔥 Super recomendo a todos realizarem todos os passos ensinados!
  
*Mensagem automática enviada utilizando Automação com Python - Selenium, PyAutoGui e Pyperclip* 🚀

*Qualquer difículdade fico a disposição* 🤖'''
pyperclip.copy(texto)

# Inserir na linha abaixo contatos ou grupos de contatos
contatos = ["+55 11 00000-0000", "Programa Trainee - 2025", "5511962696757"]
for c in contatos:
    search_box_xpath = '//div[@contenteditable="true" and @data-tab="3"]'
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, search_box_xpath))
    )
    search_box.click()
    search_box.clear()
    py.typewrite(message=c, interval=0.25)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)
    py.hotkey("ctrl", "v")
    time.sleep(2)
    btnSend = '//button[@aria-label="Send"]'
    driver.find_element(By.XPATH, btnSend).click()
driver.quit()

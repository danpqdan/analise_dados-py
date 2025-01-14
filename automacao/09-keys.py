import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url_pessoal = 'https://dsplayground.com.br'
driver = webdriver.Firefox()
driver.get("https://www.google.com/?cc=br")
time.sleep(3)
search_box = driver.find_element(By.ID, 'APjFqb')
search_box.send_keys("Copiadora BGMax")
search_box.send_keys(Keys.ENTER)
driver.execute_script(f"window.open('{url_pessoal}');")
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.execute_script(f"window.open('https://www.google.com/');")
driver.switch_to.window(driver.window_handles[2])
time.sleep(2)
a = driver.find_element(By.CLASS_NAME, "gLFyf")
a.send_keys("BGMax Exemplos Python")
a.send_keys(Keys.RETURN)

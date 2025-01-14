import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
# driver = webdriver.Chrome()
driver.get("https://www.bgmax.com.br")
driver.maximize_window()
driver.implicitly_wait(1)
try:
    element = driver.find_element(By.LINK_TEXT, 'Treinamentos')
except:
    driver.execute_script('alert("Não Achei")')
else:
    driver.execute_script('alert("Achei")')

time.sleep(10)
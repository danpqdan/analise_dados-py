import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
driver.get("http://www.bgmax.com.br")
driver.maximize_window()
time.sleep(2)
a = driver.find_element(By.LINK_TEXT, 'Copiadora')
time.sleep(2)
a.click()

# BackFoward

time.sleep(5)
driver.back()
time.sleep(5)
driver.forward()
driver.close()

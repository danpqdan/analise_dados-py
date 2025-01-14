import time

from selenium import webdriver

driver = webdriver.Edge()
driver.get("http://www.bgmax.com.br")
time.sleep(5)
driver.minimize_window()
time.sleep(5)
driver.maximize_window()
x = True
while x:
    time.sleep(5)
    x = False

import time

from selenium import webdriver

driver = webdriver.Edge()
driver.get("http://www.bgmax.com.br")
while True:
    time.sleep(10)

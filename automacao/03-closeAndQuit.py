import time

from selenium import webdriver

driver = webdriver.Edge()
url = "https://www.bgmax.com.br/exemplos-python"
driver.get(url)
driver.maximize_window()
time.sleep(5)
driver.close()

# Exemplo com Quit

driver = webdriver.Edge()
url = "https://www.bgmax.com.br/treinamentos"
driver.get(url)
driver.maximize_window()
time.sleep(5)


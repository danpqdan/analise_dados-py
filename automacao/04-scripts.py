import time

from selenium import webdriver

# Scrit com janela parametrizada ou atraves do Get()
driver = webdriver.Edge()
url_atual = "https://www.bgmax.com.br"
url_nova = "https://www.bgmax.com.br/treinamentos"
url_pessoal = "http://dsplayground.com.br"
driver.get(url_atual)
driver.maximize_window()
driver.execute_script(f"window.open('');")
time.sleep(2)
driver.switch_to.window(driver.window_handles[1])  # Muda para o windows na posicao[i]
driver.get(url_nova)
driver.execute_script(f"window.open('{url_pessoal}');")
time.sleep(2)
driver.switch_to.window(driver.window_handles[0])  # Muda para o windows na posicao[i]
time.sleep(2)
for i in range(0, 3):
    time.sleep(3)
    i += 1
driver.close()

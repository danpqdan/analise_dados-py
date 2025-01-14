import os
import time

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By

load_dotenv()
password = os.getenv('PASSWORD')
bgmax = os.getenv('BGMAX')

driver = webdriver.Firefox()
# driver.get("https://www.linkedin.com/")
# time.sleep(3)
# driver.find_element(By.CSS_SELECTOR, '.sign-in-form__sign-in-cta').click()
# driver.maximize_window()
# time.sleep(3)
# a = driver.find_element(By.XPATH, '//*[@id="username"]')
# a.send_keys('danieltisantosbackup@gmail.com')
# time.sleep(1)
# a = driver.find_element(By.XPATH, '//*[@id="password"]')
# a.send_keys(password)
# time.sleep(1)
# driver.find_element(By.XPATH, '//*[@aria-label="Sign in"]').click()
# Nova Janela

driver.execute_script(f"window.open('{bgmax}');")
driver.switch_to.window(driver.window_handles[1])
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="1432758233"]/ul/li[3]/a').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="1414058053"]').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="1947687665"]/p[22]/a').click()
driver.find_element(By.XPATH, '//*[@id="1851244771"]').click()
driver.find_element(By.ID, '85971').click()
driver.find_element(By.ID, '1002056536').send_keys('45582054812')
driver.find_element(By.ID, '1676795593').send_keys('Daniel de Jesus Santos')
driver.find_element(By.ID, '1799820343').send_keys('11962696757')
driver.find_element(By.ID, '1745687317').send_keys('danieltisantos@gmail.com')
driver.find_element(By.ID, '1437731241').send_keys('Rua ficticia')
driver.find_element(By.ID, '1660472444').send_keys('55')
driver.find_element(By.ID, '1388411638').send_keys('São Paulo')
driver.find_element(By.ID, '1601686372').send_keys('São Paulo')
driver.find_element(By.ID, '1505933642').send_keys('SP')
driver.find_element(By.ID, '1016069138').send_keys('Ensino Superior ')
driver.find_element(By.ID, '1193808284').send_keys('26/06/1997')
driver.find_element(By.ID, '1648884651').click()
driver.find_element(By.ID, '93742').click()
driver.find_element(By.ID, '1175894168').click()

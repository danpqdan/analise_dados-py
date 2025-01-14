import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
# driver = webdriver.Chrome()
driver.get("https://www.bgmax.com.br/automacao2")
driver.maximize_window()
actions = ActionChains(driver)
# actions.send_keys(Keys.TAB * 11)
nome = driver.find_element(By.ID, "1459668649")
actions.move_to_element(nome).click().send_keys("Daniel de Jesus Santos")
# actions.send_keys(Keys.TAB)
telefone = driver.find_element(By.ID, "1362265994")
actions.move_to_element(telefone).click().send_keys("11962696757")
# actions.send_keys(Keys.TAB)
email = driver.find_element(By.ID, "1804883275")
actions.move_to_element(email).click().send_keys("danieltisantos@gmail.com")
# actions.send_keys(Keys.TAB)
estadoCivil = driver.find_element(By.ID, "1587315858")
actions.move_to_element(estadoCivil).click().send_keys("Solteiro")
# actions.send_keys(Keys.TAB * 3)
submit = driver.find_element(By.ID, "1056525453")
actions.move_to_element(submit).click()
actions.perform()
time.sleep(15)
# driver.close()

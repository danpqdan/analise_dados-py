from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
driver.get("https://www.bgmax.com.br")
driver.maximize_window()
try:
    element = WebDriverWait(driver, 0.1).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="1432758233"]/ul/li[3]/a')))
    element2 = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.XPATH,
                                        '//*[@href="https://irp.cdn-website.com/146a79c7/site_favicon_16_1712607496623.ico"]')))
except:
    driver.execute_script('alert("Não achei o elemento!")')
else:
    driver.execute_script('alert("Achei o elemento!")')
finally:
    print("Fim!")

from selenium import webdriver

driver = webdriver.Edge()
# driver = webdriver.Chrome()
driver.maximize_window()
site = "https://www.bgmax.com.br/"
driver.get(site)
driver.add_cookie({"name": "Pagina", "value": "principal"})
driver.add_cookie({"name": "Cidade", "value": "Suzano-SP"})
print("\n Coockie Página")
print(driver.get_cookie("Pagina"))
print("\n Coockie Cidade")
print(driver.get_cookie("Cidade"))
print("\n Todos Coockies")
print(driver.get_cookies())
driver.delete_cookie("pagina")
driver.delete_cookie("cidade")
print("\n Todos Coockies")
print(driver.get_cookies())

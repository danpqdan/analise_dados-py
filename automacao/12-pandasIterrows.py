import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# Print do arquivo
arquivo = "/home/zenxbr/PycharmProjects/PythonProject/treiner/automacao-web/contatos.xlsx"
planilha = pd.read_excel(arquivo)
for index, row in planilha.iterrows():
    print("Index: ", index)
    print("Index da Coluna: ", row["coluna"])
    print("Nome: ", row["nome"])
    print("Telefone:", row["telefone"])
    print("E-Mail: ", row["email"])
    print("*" * 50)

# Executando arquivo
driver = webdriver.Firefox()
for index, row in planilha.iterrows():
    print(index)
    print(row["nome"])
    print(row["telefone"])
    print(row["email"])
    nome = row["nome"]
    telefone = row["telefone"]
    telefone_limpo = telefone.replace("(", "").replace(")", "").replace("-", "").replace(" ", "")
    email = row["email"]
    driver.get("https://www.bgmax.com.br/automacao")
    driver.maximize_window()
    time.sleep(3)
    # Preencher Nome
    driver.find_element(By.XPATH, '//*[@id="1459668649"]').send_keys(nome)
    # Preencher Telefone
    driver.find_element(By.XPATH, '//*[@id="1362265994"]').send_keys(telefone_limpo)
    # Preencher Email
    driver.find_element(By.XPATH, '//*[@id="1804883275"]').send_keys(email)
    time.sleep(3)
    # Clicar Submeter
    driver.find_element(By.XPATH, '//*[@id="1056525453"]').click()
    time.sleep(3)

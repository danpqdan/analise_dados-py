import ssl

import pandas as pd

ssl._create_default_https_context = ssl._create_unverified_context
planilha = pd.read_html("https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil")[1]
colunas = planilha[
    ["Unidade federativa", "Abreviação", "Área (km²)", "População (Censo 2022)", "PIB per capita (R$) (2015)",
     "Alfabetização (2016)", "Mortalidade infantil (2016)", "Expectativa de vida (2016)"]]
colunas_formatadas = colunas.rename(columns={"Unidade federativa": "Estado",
                                             "Abreviação": "UF",
                                             "Área (km²)": "Área",
                                             "População (Censo 2022)": "População",
                                             "PIB per capita (R$) (2015)": "PIB per Capita",
                                             "Alfabetização (2016)": "Alfabetização",
                                             "Mortalidade infantil (2016)": "Mortalidade infantil",
                                             "Expectativa de vida (2016)": "Longevitude"})
arquivo1 = r"/home/zenxbr/PycharmProjects/PythonProject/treiner/automacao-web/capitais.xlsx"
arquivo2 = r"/home/zenxbr/PycharmProjects/PythonProject/treiner/automacao-web/capitais.csv"
colunas_formatadas.to_excel(arquivo1, index=False)
colunas_formatadas.to_csv(arquivo2, index=False)
print("arquivos gerados")

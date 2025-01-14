import ssl

import pandas as pd

# Seleção de todas as planilhas em um HTML com a tag <table>
# ssl._create_default_https_context = ssl._create_unverified_context
# dados = pd.read_html("https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil")
# print(dados)

# Seleção de todas as planilhas em um HTML com a tag <table> na posição [0] do indice
# ssl._create_default_https_context = ssl._create_unverified_context
# dados = pd.read_html("https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil")[0]
# print(dados)

# Seleção de todas as planilhas em um HTML com a tag <table> na posição [1] com filtro de dados
ssl._create_default_https_context = ssl._create_unverified_context
dados = pd.read_html("https://pt.wikipedia.org/wiki/Unidades_federativas_do_Brasil")[1]
print("Colunas da Tabela:")
print()
for column_headers in dados.columns:
    print(column_headers)

# for index, row in dados.iterrows():
#     for coluna, conteudo in row.items():
#         print("Index: ", index)
#         print("Unidade federativa: ", row['Unidade federativa'])
#         print("Sede: ", row['Sede de governo'])
#         print("Area:", row['Área (km²)'])
#         print("Populacao: ", row['População (Censo 2022)'])
#         print("IDH: ", row['IDH (2010)'])
#         print("Mortalidade infantil: ", row['Mortalidade infantil (2016)'])
#         print("PIB per capita: ", row['PIB per capita (R$) (2015)'])
#         print("Expectativa de vida: ", row['Expectativa de vida (2016)'])
#         print("*" * 50)

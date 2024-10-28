import pandas as pd

dados = pd.read_csv("./pratica-python/Credit.csv")
print(dados.shape)  # Formato
print(dados.describe())  # resumo estatistico de colunas numericas
print(dados.head())  # primeiros registros
print(dados.tail(2))  # ultimos registros c/ parametros
print(dados[["duration"]])  # filtra por nome de coluna
print(dados.loc[1:3])  # filtra por linas de indice
print(dados.loc[[1, 3]])  # linhas 1 e 3
print(dados["purpose"] == "radio/tv")  # filtro
print(dados["credit_amount"] > 18000)  # filtro condicional

# Atibuição de resultado a uma variavel, criando um dataFrame
credito2 = dados.loc[dados["credit_amount"] > 18000]
print(credito2)
# Atibuição de resultado a uma variavel, criando um dataFrame, apenas com as colunas
credito3 = dados[["checking_status", "duration"]].loc[dados["credit_amount"] > 18000]
print(credito3)

# Séries, unica coluna
s1 = pd.Series([2, 5, 3, 34])

# Renomear
dados.rename(columns={"duration": "duração", "purpose": "proposito"}, inplace=True)
print(dados.head(1))

# Excluir coluna
dados.drop("checking_status", axis=1, inplace=True)
print(dados.head(1))

dados.isnull()  # Verifica se é nula
dados.isnull().sum()
dados.dropna()
dados["duração"] = dados["duração"].fillna(0)
dados.iloc[0:3, 0:5]

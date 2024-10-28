import pandas as pd
import seaborn as sea
import statistics as sts
import matplotlib.pyplot as plt  # Utilizado para exibir graficos no VSCode ou Editores similares


db = pd.read_csv("./tratamento-de-dados/Churn.csv", sep=";")
print(db.head())
print(db.shape)

# Nomear as colunas ->
db.columns = [
    "Id",
    "Score",
    "Estado",
    "Genero",
    "Idade",
    "Patrimonio",
    "Saldo",
    "Produtos",
    "TemCartCredito",
    "Ativo",
    "Salario",
    "Saiu",
]

print(db.head())


def verificarDados():
    # Explorar dados da categoria 'estado'
    agrupado = db.groupby(["Estado"]).size()
    agrupado
    agrupado.plot.bar(color="gray")
    plt.show()

    # Explorar dados da categoria genero
    agrupado = db.groupby(["Genero"]).size()
    agrupado
    agrupado.plot.bar(color="red")
    plt.show()

    # Explorar dados da categoria escore
    print(db["Score"].describe())
    sea.boxplot(db["Score"]).set_title("Score")
    # sea.distplot(db["Score"]).set_title("Score") => Func depreciado, alternativa abaixo =>
    sea.histplot(db["Score"], kde=True).set_title("Score")
    plt.show()

    # Explorar dados de idade
    print(db["Idade"].describe())
    sea.boxplot(db["Idade"]).set_title("Idade")
    sea.histplot(db["Idade"], kde=True).set_title("Idade")
    plt.show()

    # Explorar dados de Saldo
    print(db["Saldo"].describe())
    sea.boxplot(db["Saldo"]).set_title("Saldo")
    sea.histplot(db["Saldo"], kde=True).set_title("Saldo")
    plt.show()

    # Explorar dados de Salario
    print(db["Salario"].describe())
    sea.boxplot(db["Salario"]).set_title("Salario")
    sea.histplot(db["Salario"], kde=True).set_title("Salario")
    plt.show()


verificarDados()
# Contaremos valor NAN NotANumber
print(db.isnull().sum())  # verificar colunas que possuem NAN
print(db["Salario"].describe())

mediana = sts.median(db["Salario"])
mediana
# db["Salario"].fillna(mediana, inplace=True)  # FeatureWarning pois cria uma copia intermediaria, Correção abaixo
db["Salario"] = db["Salario"].fillna(mediana)
print(db["Salario"].isnull().sum())  # Verificar os dados NAN

# genero, Falta de padronização e NANs
agrupado = db.groupby(["Genero"]).size()
agrupado
print(db["Genero"].isnull().sum())  # Total de NANs
# db["Genero"].fillna("Masculino", inplace=True)  # FeatureWarning pois cria uma copia intermediaria, Correção abaixo
db["Genero"] = db["Genero"].fillna("Masculino")
print(db["Genero"].isnull().sum())  # Verificar os NANs novamente

# Padronização de elementos da coluna
db.loc[db["Genero"] == "M", "Genero"] = "Masculino"
db.loc[db["Genero"].isin(["Fem", "F"]), "Genero"] = "Feminino"
# Visualizar o resultado
agrupado = db.groupby(["Genero"]).size()
print(agrupado)

# Idades fora do dominio
print(db["Idade"].describe())
db.loc[(db["Idade"] < 0) | (db["Idade"] > 120)]
mediana = sts.median(db["Idade"])  # Calcular media
print(mediana)
db.loc[(db["Idade"] < 0) | (db["Idade"] > 120), "Idade"] = mediana  # Substituir
print(db.loc[(db["Idade"] < 0) | (db["Idade"] > 120)])  # Localizar se ainda existem
agrupado = db.groupby(["Idade"]).size()
print(agrupado)

# Dados duplicados pelo ID
db[db.duplicated(["Id"], keep=False)]
db.drop_duplicates(subset="Id", keep="first", inplace=True)
print(db[db.duplicated(["Id"], keep=False)])

# Estados fora do Dominio
agrupado = db.groupby(["Estado"]).size()
print(agrupado)
# Atribuindo MODA
db.loc[db["Estado"].isin(["RP", "SP", "TD"]), "Estado"] = "RS"
agrupado = db.groupby(["Estado"]).size()
print(agrupado)  # Verificar resultado

# Outliers em salario, considerando 2 desvios padrão
desv = sts.stdev(db["Salario"])
print(desv)
db.loc[db["Salario"] >= 2 * desv]
mediana = sts.median(db["Salario"])
print(mediana)
db.loc[db["Salario"] >= 2 * desv, "Salario"] = mediana  # Atribuição
db.loc[db["Salario"] >= 2 * desv]
plt.show()
print(db.head())
print(db.shape)
verificarDados()

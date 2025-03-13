import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

base = pd.read_csv("./trees.csv")

# Criando um boxplot para a coluna 'Volume' no conjunto de dados
# O boxplot é horizontal (vert=False), não mostra outliers (showfliers=False),
# possui um entalhe para indicar o intervalo de confiança ao redor da mediana (notch=True),
# e usa patch_artist=True para permitir preenchimento de cor personalizado.
plt.boxplot(base.Volume, vert=False, showfliers=False, notch=True, patch_artist=True)
plt.title("Árvores")
plt.xlabel("Volume")
plt.show()

# Criando um boxplot para todo o conjunto de dados
# O boxplot é padrão, sem configurações adicionais.
plt.boxplot(base)
plt.title("Árvores")
plt.xlabel("Dados")
plt.show()

plt.boxplot(base.Volume, vert=False)
plt.boxplot(base.Girth, vert=False)
plt.boxplot(base.Height, vert=False)
plt.title("Árvores")
plt.xlabel("Volume")
plt.show()
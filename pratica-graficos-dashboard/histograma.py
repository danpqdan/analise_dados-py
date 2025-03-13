import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

# Carregando a base de dados
base = pd.read_csv("./trees.csv")
base.shape

# Dados
print(base.head())

 # Calcula o histograma da segunda coluna do DataFrame, dividindo os dados em 6 intervalos
 # Imprime os resultados do histograma, que incluem as contagens de frequência e os limites dos intervalos 
h = np.histogram(base.iloc[:,1], bins = 6)
print(h)

# Visualização do histograma com a biblioteca matplotlib
plt.hist(base.iloc[:,1], bins = 6)
plt.title("Árvores")
plt.ylabel("Frequência")
plt.xlabel("Altura")
plt.show(block=True)


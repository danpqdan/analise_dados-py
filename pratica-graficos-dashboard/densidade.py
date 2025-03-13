import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando a base de dados
base = pd.read_csv("./trees.csv")

plt.hist(base.iloc[:,1], bins = 6)
sns.histplot(base.iloc[:,1], bins = 6, kde = False, color='blue').set(title='Árvores')
plt.show()

# Densidade, metodo kdeplot para densidade
sns.kdeplot(base.iloc[:,1], color='blue').set(title='Árvores')
plt.show()

# Densidade e histograma
sns.histplot(base.iloc[:,1], bins = 6, kde = True, color='blue').set(title='Árvores')
plt.show()


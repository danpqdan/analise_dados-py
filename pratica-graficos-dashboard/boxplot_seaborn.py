import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

# Carregando a base de dados
base = pd.read_csv("./trees.csv")

# Boxplot
sns.boxplot(base.Volume, orient='v').set_title('Árvores')
plt.show()

# Boxplot para todas as colunas
sns.boxplot(data=base)
plt.show()

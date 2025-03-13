import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

base = pd.read_csv("./co2.csv")

# Variaveis categorias para X e Y
x = base.conc
y = base.uptake

unicos = list(set(base.Treatment))
print(unicos)

for i in range(len(unicos)):
    indice = base.Treatment == unicos[i]
    plt.scatter(x[indice], y[indice], label = unicos[i])

plt.legend(loc = 'lower right')
plt.show()
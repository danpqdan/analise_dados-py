import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

base = pd.read_csv("./insect.csv")
print(base.shape)

print(base.head())

# Agrupamento dos dados com groupby
agrupamento = base.groupby(['spray'])['count'].sum()
print(agrupamento)

# Gráfico de barras
agrupamento.plot.bar(color = 'gray')
plt.show()

# Gráfico de barras com cores diferentes
agrupamento.plot.bar(color = ['blue', 'yellow', 'red', 'green', 'pink', 'orange'])
plt.show()

# Gráfico de pizza
agrupamento.plot.pie()
agrupamento.plot.pie(legend=True)
plt.show()
      


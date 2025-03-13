import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

base = pd.read_csv("./trees.csv")

sns.histplot(base.Volume, color='blue', kde=True, stat='density', bins=10).set(title='Volume')
plt.show()

base2 = pd.read_csv("./chicken.csv")
print(base2.head())

agrupado = base2.groupby(['feed'])['weight'].sum()
print(agrupado)

teste = base2.loc[base2['feed'] == 'horsebean']
print(teste)


plt.figure(1)
plt.subplot(3,2,1)
sns.histplot(base2.loc[base2['feed'] == 'horsebean'].weight).set(title='horsebean')
plt.subplot(3,2,2)
sns.histplot(base2.loc[base2['feed'] == 'casein'].weight, kde=True).set(title='casein')
plt.subplot(3,2,3)
sns.histplot(base2.loc[base2['feed'] == 'linseed'].weight, kde=True).set(title='linseed')
plt.subplot(3,2,4)
sns.histplot(base2.loc[base2['feed'] == 'meatmeal'].weight, kde=True).set(title='meatmeal')
plt.subplot(3,2,5)
sns.histplot(base2.loc[base2['feed'] == 'soybean'].weight, kde=True).set(title='soybean')
plt.subplot(3,2,6)
sns.histplot(base2.loc[base2['feed'] == 'sunflower'].weight, kde=True).set(title='sunflower')
plt.tight_layout()
plt.show()





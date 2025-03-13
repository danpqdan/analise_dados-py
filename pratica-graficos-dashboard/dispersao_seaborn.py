import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

base = pd.read_csv("./co2.csv")

sns.scatterplot(x=base.conc, y=base.uptake, hue = base.Type)
q = base.loc[base['Type'] == 'Quebec']
m = base.loc[base['Type'] == 'Mississippi']

plt.figure()
plt.subplot(1,2,1)
sns.scatterplot(x=q.conc, y=q.uptake).set_title('Quebec')
plt.subplot(1,2,2)
sns.scatterplot(x=m.conc, y=m.uptake).set_title('Mississippi')
plt.show()

ch = base.loc[base['Treatment'] == 'chilled']
nc = base.loc[base['Treatment'] == 'nonchilled']
plt.figure()
plt.subplot(1,2,1)
sns.scatterplot(x=ch.conc, y=ch.uptake).set_title('Chilled')
plt.subplot(1,2,2)
sns.scatterplot(x=nc.conc, y=nc.uptake).set_title('Non Chilled')
plt.show()

base2 = pd.read_csv("./esoph.csv")
sns.catplot(x='alcgp', y='ncontrols', data=base2, jitter=False)
plt.show()

sns.catplot(x='alcgp', y='ncontrols', data=base2, col='tobgp')
plt.show()
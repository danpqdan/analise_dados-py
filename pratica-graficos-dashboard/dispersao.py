import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

base = pd.read_csv("./trees.csv")

plt.scatter(base.Girth, base.Volume, color = 'blue', facecolors='none', marker='*')
plt.title("Árvores")
plt.xlabel("Circunferencia")
plt.ylabel("Volume")
plt.show()

plt.plot(base.Girth, base.Volume)
plt.title("Árvores")
plt.xlabel("Circunferencia")
plt.ylabel("Volume")
plt.show()

sns.regplot(x=base.Girth, y=base.Volume, data = base, x_jitter=0.3, fit_reg=False)
plt.show()
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import seaborn as sns

base = pd.read_csv("./trees.csv")

plt.scatter(base.Girth, base.Volume)
plt.scatter(base.Girth, base.Height)
plt.scatter(base.Height, base.Volume, marker='*')

plt.figure(1)
plt.subplot(2,2,1)
plt.scatter(base.Girth, base.Volume)
plt.subplot(2,2,2)
plt.scatter(base.Girth, base.Height)
plt.subplot(2,2,3)
plt.scatter(base.Height, base.Volume, marker='*')
plt.subplot(2,2,4)
plt.hist(base.Volume)
plt.show()
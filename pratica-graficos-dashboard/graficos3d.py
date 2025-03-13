import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

base = pd.read_csv("./orchard.csv")

figura = plt.figure()
eixo = figura.add_subplot(1,1,1, projection = '3d')
eixo.scatter(base.decrease, base.rowpos, base.colpos)
eixo.set_xlabel("decrease")
eixo.set_ylabel("rowpos")
eixo.set_zlabel("colpos")
plt.show()
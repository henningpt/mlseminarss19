import numpy as np
import pandas as pd

from pandas.plotting import scatter_matrix
from matplotlib import pyplot as plt


# test
print("test1")
data = pd.read_csv("dataset/dataset.csv")
df = pd.DataFrame(data=data)

plt.plot(df["longitude"], df["latitude"], "x")
plt.show()
print("test2")

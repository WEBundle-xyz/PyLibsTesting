import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import bootstrap_plot
from rich import print

print("_"*40)

dev_x = [25, 26, 27, 27, 29, 34, 38]
dev_y = [3489, 3495, 4323, 5432, 6543, 7654, 8763]

plt.plot(dev_x, dev_y)

plt.show()

print("_"*40)
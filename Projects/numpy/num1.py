import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import bootstrap_plot
from rich import print

print("_"*40)

data = pd.Series(np.random.rand(1000))
bootstrap_plot(data, size=50, samples=500, color="grey")

print("_"*40)
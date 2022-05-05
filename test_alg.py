import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.tsaplots import plot_acf


df = pd.read_csv('Dataset/Adana/AdanaAverageDF.csv', index_col='Date')
df.index = pd.to_datetime(df.index)

df.plot()
plt.show()
print(df.columns)
print(type(df.index))
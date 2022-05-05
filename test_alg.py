import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.graphics.tsaplots import plot_acf


data = pd.read_csv('Dataset/Adana/AdanaAverageDF.csv', index_col='Date')
data.index = pd.to_datetime(data.index)
data = data.loc[data.index >= '2022-03-01']
data = data.resample('D').mean()

data.plot()
plt.show()
print(data.columns)
print(type(data.index))
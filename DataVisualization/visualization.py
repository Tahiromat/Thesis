
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/Kocaeli/KocaeliAverageDF.csv')
df = df[:-1]
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S.%f')

name_list = df.columns[1:]
for name in name_list:
    sns.scatterplot(data=df, x='Date', y=name)
    plt.title(name)
    plt.grid()
    plt.show()
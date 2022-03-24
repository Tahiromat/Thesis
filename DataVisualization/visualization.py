
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/Adana/AdanaAverageDF.csv')
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S')
print(df.info())
print(df)
name_list = df.columns[1:]
for name in name_list:

    sns.scatterplot(data=df, x='Date', y=name)
    plt.title(name)
    plt.grid()
    plt.show()
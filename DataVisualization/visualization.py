'''
type of visualizations will be writed functially under visualization class and then you will use that functions in the app file.
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



df2 = pd.read_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/Ankara/test.csv')
df2['Tarih'] = pd.to_datetime(df2['Tarih'])

names = df2.columns[1:]

for name in names:
    sns.scatterplot(data=df2, x='Tarih', y=name)
    plt.title(f'{name} Based Date')
    plt.show()


print(df2.info())
'''
    İf we can not add new columns for missing datasets where df columns are not the same then
    For visualization we need a method. Firstly for visualization ve need thee check names inside the columns based on them we need the visualize
'''
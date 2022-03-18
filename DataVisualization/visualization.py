'''
type of visualizations will be writed functially under visualization class and then you will use that functions in the app file.
'''
'''
    Here: Cities subfiles will be merged based on their .mean() values. And save the merged file as name: mean$cityname.csv
''' 
from operator import index
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/test.csv'

df = pd.read_csv(DATA_PATH)
df['Tarih'] = pd.to_datetime(df['Tarih'])

print(df.info())

def create_new_df_from_mean_of_subcities():
    names = df.columns[1:]
    for name in names:
        print(name)
        if df[name].mean() != 0:
            sns.scatterplot(data=df, x='Tarih', y=name)
            plt.title(f'{name} Based Date')
            plt.show()
        else:
            pass

    print(df.info())

create_new_df_from_mean_of_subcities()

'''
    İf we can not add new columns for missing datasets where df columns are not the same then
    For visualization we need a method. Firstly for visualization ve need thee check names inside the columns based on them we need the visualize
'''
'''
    type of visualizations will be writed functially under visualization class and then you will use that functions in the app file.

    Here: Cities subfiles will be merged based on their .mean() values. And save the merged file as name: mean$cityname.csv
''' 

from operator import index
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/Ankara/ankara1.csv'

df = pd.read_csv(DATA_PATH)
df['Tarih'] = pd.to_datetime(df['Tarih'])

def visualize_df_columns():
    names = df.columns[1:]
    for name in names:
        if df[name].mean() != 0:
            sns.lineplot(data=df, x='Tarih', y=name)
            plt.title(f'{name} Based Date')
            plt.show()
        else:
            pass

visualize_df_columns()


import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


DATA_PATH = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/Kocaeli'

df1 = pd.read_csv(DATA_PATH + '/kocaeli1.csv')
df2 = pd.read_csv(DATA_PATH + '/kocaeli2.csv')

df1['Tarih'] = pd.to_datetime(df1['Tarih'])
df2['Tarih'] = pd.to_datetime(df2['Tarih'])

df3 = pd.read_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/Ankara/ankara1.csv')
df3['Tarih'] = pd.to_datetime(df3['Tarih'])

df4 = pd.concat([df1, df2, df3], ignore_index=True)
df4 = df4.groupby('Tarih').mean()
df4.to_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/test.csv')


print(df4)
import pandas as pd



import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/Kocaeli'

df1 = pd.read_csv(DATA_PATH + '/kocaeli1.csv')
df2 = pd.read_csv(DATA_PATH + '/kocaeli2.csv')

df1['Tarih'] = pd.to_datetime(df1['Tarih'])
df2['Tarih'] = pd.to_datetime(df2['Tarih'])

df_list = [df1, df2]
df3 = pd.concat([df1, df2], ignore_index=False)
df3 = df3.groupby('Tarih').mean()
df3.to_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/tsest.csv')



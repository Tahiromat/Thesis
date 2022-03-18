'''
    Here: Cities subfiles will be merged based on their .mean() values. And save the merged file as name: mean$cityname.csv
''' 
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

DATA_PATH = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/Kocaeli'

# df1 = pd.read_csv(DATA_PATH + '/ankara1.csv')
# df2 = pd.read_csv(DATA_PATH + '/ankara2.csv')

# df1['Tarih'] = pd.to_datetime(df1['Tarih'])
# df2['Tarih'] = pd.to_datetime(df2['Tarih'])

def create_new_df_from_mean_of_subcities():
    # os.chdir(old_subfolder_path + '/' + city_name)
    # for f in os.listdir():
    #     print(f)

    df1 = pd.read_csv(DATA_PATH + '/kocaeli1.csv')
    df2 = pd.read_csv(DATA_PATH + '/kocaeli2.csv')

    df1['Tarih'] = pd.to_datetime(df1['Tarih'])
    df2['Tarih'] = pd.to_datetime(df2['Tarih'])

    df_list = [df1, df2]
    df3 = pd.concat([df1, df2], ignore_index=False)
    df3 = df3.groupby('Tarih').mean()
    
    return df3.to_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/tsest.csv')




create_new_df_from_mean_of_subcities()




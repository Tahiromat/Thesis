import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def __create_new_df_from_mean_of_subcities(old_subfolder_path, city_name):
    df_list = []
    os.chdir(old_subfolder_path + '/' + city_name)
    for f in os.listdir():
        data_path = old_subfolder_path + '/' + city_name + '/' + f
        df = pd.read_csv(data_path)
        df['Tarih'] = pd.to_datetime(df['Tarih'])
        df_list.append(df)
    df_new = pd.concat([df_list[0], df_list[1]], ignore_index=True)
    df_new = df_new.groupby('Tarih').mean()
    return df_new.to_csv(old_subfolder_path + '/' + city_name + '/' + city_name +'AverageDF.csv')

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def create_new_df_from_mean_4all_subcities(main_path):
    print('\n\nCreating new dataset for mean of the city......................................................... \n')
    os.chdir(main_path)
    for city_name in os.listdir():
        __create_new_df_from_mean_of_subcities(main_path, city_name)

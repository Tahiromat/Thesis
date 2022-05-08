import os
import time
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def __create_new_df_from_mean_of_subcities(main_path, city_name):
    df_list = []
    os.chdir(main_path + '/' + city_name)
    for f in os.listdir():
        data_path = main_path + '/' + city_name + '/' + f
        df = pd.read_csv(data_path)
        df_list.append(df)
    df_new = pd.concat(df_list, ignore_index=True)
    df_new = df_new.groupby('Date').mean()
    return df_new.to_csv(main_path + '/' + city_name + '/' + city_name +'AverageDF.csv')

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def create_new_df_from_mean_4all_subcities(main_path):
    print('\n\nCreating new dataset for mean of the city......................................................... \n')
    os.chdir(main_path)
    for city_name in os.listdir():
        print(f'Creating average df for : {city_name}')
        __create_new_df_from_mean_of_subcities(main_path, city_name)
        print(f'{city_name} : Average df is successfully created\n')

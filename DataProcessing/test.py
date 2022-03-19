from hashlib import new
from operator import le
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dfbos = pd.read_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Fake_Data/bos_fake.csv')
df1 = pd.read_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Fake_Data/ankara_fake.csv')
df2 = pd.read_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Fake_Data/kocaeli_fake.csv')
df3 = pd.read_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Fake_Data/istanbul_fake.csv')
df4 = pd.read_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Fake_Data/mersin_fake.csv')

# df_10 = pd.concat([dfbos,df1, df2], ignore_index=True)
# df_10 = df_10.groupby('Tarih').mean()
# print(df_10)


def merge_all_sub_df(df_liste):
    conatted_list = []
    for index in range(0, len(df_liste), 1):
        df_new = pd.concat(df_liste, ignore_index=True)
        conatted_list.append(df_new)

    return conatted_list
    # df_new.to_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/AverageDF.csv')

df_list = [df1, df2]
lst = merge_all_sub_df(df_list)

print(lst)

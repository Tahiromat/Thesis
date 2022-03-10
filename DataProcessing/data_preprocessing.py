# ONE BY ONE
#  Read the data
#  Convert data to dataframe (Dont forget DateTime fow index column)
#  Fill NaN values with mean value of the column
#  Convert all values between 0-1
#  Concat the all files in one new df
#  Use groubby method on the new df based on time values (Get mean of the variables)

from click import style
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

from change_dtype import change_dtype_utility

sub_df_path = 'RawData/Kocaeli/alikahyamthm.csv'

def __preprocess_sub_csv_file(sub_df_path):

    df = pd.read_csv(sub_df_path)
    df['Tarih'] = pd.to_datetime(df['Tarih'])
    # df = df.set_index("Tarih")

    ''' Metod yazilacak: 
        Metodun yapilmasi istenen islemi 
            Nan degerlerin olduğu kolon tamamiyle bos degilse; nan degerler yerine o kolonun ortalamasini ata.
            Eger Nan degerin oldugu kolon tamamen bos ise; nan degerleri yerine 0 degerini ata.
    '''

    print(f'\n\n...................    DF  LOADING   ............................................') 
    print(f'\n\n{df}') 

    print(f'\n\n...................    DF  INFO   ............................................\n\n') 
    print(f'\n\n{df.info()}', ) 

    
    total_column_names = df.columns
    total_column_names = total_column_names[1:]

    for name in total_column_names:
        
        df[name] = change_dtype_utility(df, name, '-', '0')
        df[name] = change_dtype_utility(df, name, ',', '.')
        # df[name] = change_dtype_utility(df, name, '-', df[name].mean())
        # df[name] = df[name].astype(str).str.replace(',','.')
        df[name] = df[name].astype(float)

    
    print(f'\n\n...................    DF  INFO   ............................................\n\n') 
    print(f'\n\n{df.info()}', ) 

    print(f'\n\n...................    DF  PLOTTING   ............................................\n\n') 
    plt.figure(figsize = (15,8))
    sns.scatterplot(x = 'Tarih', y = 'PM 2.5 ( µg/m3 )', data = df)
    sns.lineplot(x = 'Tarih', y = 'SO2 ( µg/m3 )', data = df)
    plt.show()

    return df




def __read_subfiles_path_and_preprocess():

    '''
        Burada belirli bir dosya altindaki her bir csv dosyasi sirasiyla daha önce tek dosya acip ön işleme adimlari uygulanan fonsiyondan geçirilecek böylece ayni dosya altindaki herbir csv dosyasi veri ön işleme adimlarini tamamlamis olacaktir. 
    '''
    __preprocess_sub_csv_file(sub_df_path)


def read_folder_path_and_preprocess():
    '''
        Burada raw data altindaki bütün dosyalar tek tek gezilerek acilan dosya icerisinde read_subfiles_path_and_preprocess fonksiyonu döndürülecektir.
    '''
    __read_subfiles_path_and_preprocess()

read_folder_path_and_preprocess()
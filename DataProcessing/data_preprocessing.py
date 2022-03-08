# ONE BY ONE
#  Read the data
#  Convert data to dataframe (Dont forget DateTime fow index column)
#  Fill NaN values with mean value of the column
#  Convert all values between 0-1
#  Concat the all files in one new df
#  Use groubby method on the new df based on time values (Get mean of the variables)



import pandas as pd
import numpy as np

sub_df_path = 'RawData/Kocaeli/alikahyamthm.csv'

def __preprocess_sub_csv_file(sub_df_path):

    df = pd.read_csv(sub_df_path)
    df['Tarih'] = pd.to_datetime(df['Tarih'])

    ''' Fonksiyon yazilacak: 
        Fonsiyonun yapilmasi istenen islem 
            Nan degerlerin olduğu kolon tamamiyle bos degilse; nan degerler yerine o kolonun ortalamasini ata.
            Eger Nan degerin oldugu kolon tamamen bos ise; nan degerleri yerine 0 degerini ata.
    '''
    
    print(f'\n\n{df.describe().T}') 
    print(f'\n\n{df.head()}') 
    print(f'\n\n{df.columns.unique()}') 
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

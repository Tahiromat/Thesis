'''
    Here: Cities subfiles will be merged based on their .mean() values. And then you will save the merged file under Dataset folder with the same folder name..
''' 
import pandas as pd
from preprocess_file import preprocess_sub_csv_file


Path = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/RawData/Istanbul'

def create_mean_df():

    df1 = preprocess_sub_csv_file('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/RawData/Istanbul/kandira.csv')
    df2 = preprocess_sub_csv_file('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/RawData/Istanbul/körfez.csv')

    total_dataframes = [df1, df2]

    new_df = pd.concat(total_dataframes, ignore_index=True)

    print(f"\n\nDF1 ............................. \n\n{df1}\n\n")
    print(f"\n\nDF2 ............................. \n\n{df2}\n\n")
    print(f"\n\nNEWDF ............................. \n\n{new_df}\n\n")


create_mean_df()
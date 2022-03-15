import pandas as pd
from read_csv_and_change_dtype import change_dtype_utility, read_csv_files


# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def preprocess_sub_csv_file(csv_file_path):

    df = read_csv_files(csv_file_path)

    total_column_names = df.columns
    total_column_names = total_column_names[1:]

    for name in total_column_names:

        df[name] = change_dtype_utility(df, name, '-', '0')
        df[name] = change_dtype_utility(df, name, '.', '')
        df[name] = change_dtype_utility(df, name, ',', '.')
        df[name] = df[name].astype(float)

    # print(f'{df.info()}')
    
    return df


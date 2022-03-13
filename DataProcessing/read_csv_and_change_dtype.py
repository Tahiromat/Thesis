import pandas as pd

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def read_csv_files(csv_file_path):
    df =  pd.read_csv(csv_file_path)
    df['Tarih'] = pd.to_datetime(df['Tarih'])
    return df


# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def change_dtype_utility(df, name, current_param, replaced_param):
    
    return df[name].astype(str).str.replace(current_param,replaced_param)

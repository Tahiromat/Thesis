import os
import time
import pandas as pd
import warnings
warnings.simplefilter("ignore")

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def __change_dtype_utility(df, name, current_param, replaced_param):
    return df[name].astype(str).str.replace(current_param,replaced_param, regex=True)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def __preprocess_all_csv_files(df):
    # df = data_frame
    total_column_names = df.columns
    total_column_names = total_column_names[1:]
    for name in total_column_names:
        df[name] = __change_dtype_utility(df, name, '-', '0')
        df[name] = __change_dtype_utility(df, name, '.', '')
        df[name] = __change_dtype_utility(df, name, ',', '.')
        df[name] = df[name].astype(float)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def __preprocess_scraped_exel_file(downloaded_path, new_path_to_go, file):
    df = pd.read_excel(downloaded_path + '/' + file)
    file_name = df.columns[1]
    file_name = file_name.replace('/', '')
    file_name = file_name.replace('.', '')
    file_name = file_name.replace('-', '')
    real_columns = df.loc[0]
    df.columns = real_columns
    df.drop(labels=0, axis=0, inplace=True)
    df.columns=df.columns.astype(str)
    df.rename(columns={'NaT':'Date'}, inplace=True)
    __preprocess_all_csv_files(df)
    
    os.chdir(new_path_to_go)
    for city_name in os.listdir():
        if city_name == file_name.split(' ')[0]:
            new_file_name = file_name.replace(' ', '_')
            new_file_name = new_file_name.lower()
            print(f'Loading df is : {new_file_name} ')
            df.to_csv(new_path_to_go + '/' + city_name + '/' + new_file_name + '.csv', index=False)
            print(f'{new_file_name} : Successfuly uploaded\n')
    #!!!!!!!!!!!!!!!!  Here check if the new file already exist under dataset/uniq city file then concat new and old file based on Date column. 

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def __clear_old_csv_files(downloaded_path):
#     os.chdir(downloaded_path)
#     for file in os.listdir():
#         if file.endswith('.csv'):
#             os.remove(file)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def send_preprocess_scraped_exel2csv_files_dataset_folder(downloaded_path, new_path_to_go):
    print('\n\nNew csv file is loading under uniq cities.........................................................\n')
    os.chdir(downloaded_path)
    for file in os.listdir():
        if file.startswith('Veri Detayları') and file.endswith('.xlsx'):
            __preprocess_scraped_exel_file(downloaded_path, new_path_to_go, file)
            time.sleep(1)
        else:
            os.remove(file)
            time.sleep(1)

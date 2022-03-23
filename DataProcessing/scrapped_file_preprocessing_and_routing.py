import os
import time
import pandas as pd
import warnings
warnings.simplefilter("ignore")

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def __change_dtype_utility(df, name, current_param, replaced_param):
    return df[name].astype(str).str.replace(current_param,replaced_param, regex=True)

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def __preprocess_all_csv_files(df):
    # df = data_frame
    total_column_names = df.columns
    total_column_names = total_column_names[1:]
    for name in total_column_names:
        df[name] = __change_dtype_utility(df, name, '-', '0')
        df[name] = __change_dtype_utility(df, name, '.', '')
        df[name] = __change_dtype_utility(df, name, ',', '.')
        df[name] = df[name].astype(float)

# def create_uniq_route4save_csv_files(df, new_path, filename, save_typet):
#     '''
#         Here check file name and send it to same name folder under Dataset
#     '''
#     df.to_csv(new_path_to_go + filename + save_typet, index=False)
#     pass

def __preprocess_scraped_exel_file(downloaded_path, new_path_to_go, file):
    df = pd.read_excel(downloaded_path + '/' + file)
    file_name = df.columns[1]
    file_name = file_name.replace('/', ' ')
    file_name = file_name.replace('.', ' ')
    real_columns = df.loc[0]
    df.columns = real_columns
    df.drop(labels=0, axis=0, inplace=True)
    df.columns=df.columns.astype(str)
    df.rename(columns={'NaT':'Date'}, inplace=True)
    __preprocess_all_csv_files(df)
    
    os.chdir(new_path_to_go)
    for city_name in os.listdir():
        if city_name == file_name.split(' - ')[0]:
            df.to_csv(new_path_to_go + '/' + city_name + '/' + file_name + '.csv', index=False)

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def __clear_old_csv_files(downloaded_path):
#     os.chdir(downloaded_path)
#     for file in os.listdir():
#         if file.endswith('.csv'):
#             os.remove(file)

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def send_preprocess_scraped_exel2csv_files_dataset_folder(downloaded_path, new_path_to_go):
    print('\n\nNew csv wile is loading under uniq cities......................................................... ')
    os.chdir(downloaded_path)
    # __clear_old_csv_files(downloaded_path)
    for file in os.listdir():
        if file.startswith('Veri Detayları') and file.endswith('.xlsx'):
            __preprocess_scraped_exel_file(downloaded_path, new_path_to_go, file)
            time.sleep(1)
        else:
            os.remove(file)
            time.sleep(1)

# downloaded_path = '/home/tahir/Downloads/'
# new_path_to_go = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/'

# send_preprocess_scraped_exel2csv_files_dataset_folder(downloaded_path, new_path_to_go)


# For copying the files --> https://stackoverflow.com/questions/3397752/copy-multiple-files-in-python

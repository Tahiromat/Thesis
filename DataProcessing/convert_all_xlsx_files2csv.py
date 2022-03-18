import os
import pandas as pd

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def __read_excel_file(raw_path, raw_name):
    return pd.read_excel(f'{raw_path}/{raw_name}.xlsx')

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def __convert_xlsx2csv(df, path, save_name):
    df.to_csv(f'{path}/{save_name}.csv', index=None, header=True)

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def __subfolder_convert_and_save_files(main_folder_path, city_name):
    os.chdir(main_folder_path + '/' + city_name)
    for f in os.listdir():
        f_name, f_ext = os.path.splitext(f)
        if f_ext == '.xlsx':
            __convert_xlsx2csv(__read_excel_file(main_folder_path + '/' + city_name, f_name), main_folder_path + '/' + city_name, f_name)

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def find_subcities_convert2csv_save(main_folder_path):
    print('\n\nAll .xlsx files converting to .csv file......................................................... ')
    for city_name in os.listdir(main_folder_path):
        __subfolder_convert_and_save_files(main_folder_path, city_name)

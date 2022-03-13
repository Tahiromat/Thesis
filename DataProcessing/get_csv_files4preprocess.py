from operator import index
from read_and_convert_file import convert_xlsx2csv, read_excel_file
from preprocess_file import preprocess_sub_csv_file
import pandas as pd
import os 


'''
    Burada önce her bir dosya içindeki csv dosyalari preprocess methodundan geçirilecek daha sonra bu method bir başka method olan klasor için dosyalarin içinde gezinmesi için kullanilacak.
'''

# main_folder = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/RawData'

MAIN_FOLDER_PATH = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/RawData'



def __subfolder_preprocess(main_folder_path, city_name):

    os.chdir(main_folder_path + '/' + city_name)

    for f in os.listdir():

        f_name, f_ext = os.path.splitext(f)
        if f_ext == '.csv':

            # print(f_name)
            # print(f_ext)

            csv_path = main_folder_path + '/' + city_name + '/' + f_name + '.csv'
            # file_paths.append(csv_path)
            print(csv_path)

            # preprocess_sub_csv_file(csv_path)

    # print(file_paths)



def find_subcities4preprocess(main_folder_path):

    for city_name in os.listdir(main_folder_path):

        __subfolder_preprocess(main_folder_path, city_name)


find_subcities4preprocess(MAIN_FOLDER_PATH)
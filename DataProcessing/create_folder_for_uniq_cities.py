'''
    That methods will creates new city folders based on csv files (FOR UNIQ CITIES) --> under Dataset Folder.
'''
import os 
import pandas as pd
import warnings
warnings.simplefilter("ignore")

# # That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def make_list_for_uniq_cities(downloaded_path):
    unique_cities_list = []
    os.chdir(downloaded_path)
    for f in os.listdir():
        if f.endswith('.xlsx'):
            df = pd.read_excel(downloaded_path + '/' + f)
            file_name = df.columns[1]
            file_name = file_name.replace('/', ' ')
            file_name = file_name.replace('.', ' ')
            file_name = file_name.split(' - ')[0]
            unique_cities_list.append(file_name)
            # print(file_name)
    #     file_name, file_ext = os.path.splitext(file)
    #     if file.endswith('.csv'):
    #         filename = file.split(' - ')
    #         city_name = filename[0]
    #         unique_cities_list.append(city_name)
    #         if city_name.endswith('.csv'):
    #             city_name = city_name.split('.')
    #             city_name = city_name[0]
    #             unique_cities_list.append(city_name)
    # for city in unique_cities_list:
    #     if city.endswith('.csv'):
    #         unique_cities_list.remove(city)
    return unique_cities_list

# # That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def create_folder_with_uniq_cities(file_downloaded_path, cities_create_path):
    print('\n\nCreating uniq cities......................................................... ')
    cities_list = lst = make_list_for_uniq_cities(file_downloaded_path)
    for city in cities_list:
        file_name_and_path = cities_create_path + '/' + city
        if not os.path.exists(file_name_and_path):
            os.makedirs(file_name_and_path)
            print(f'Created new directory : {file_name_and_path} ')
        else:
            print(f'Directory already exist : {file_name_and_path} ')


# CITIES_CREATE_PATH = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset'
# FILE_DOWNLOADED_PATH = '/home/tahir/Downloads/'

# make_list_for_uniq_cities(FILE_DOWNLOADED_PATH)
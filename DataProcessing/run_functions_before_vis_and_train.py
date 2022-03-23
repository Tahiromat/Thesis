import pandas as pd
# from convert_all_xlsx_files2csv import find_subcities_convert2csv_save
# from preprocess_all_csv_file import find_subcities_preprocess_and_saveas_new_folder
# from datasets_merging import create_new_df_from_mean_4all_subcities
from create_folder_for_uniq_cities import create_folder_with_uniq_cities
from scrapped_file_preprocessing_and_routing import send_preprocess_scraped_exel2csv_files_dataset_folder

MAIN_FOLDER_PATH = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/RawData'
NEW_PATH = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset'
CITIES_CREATE_PATH = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset'
FILE_DOWNLOADED_PATH = '/home/tahir/Downloads/'

downloaded_path = '/home/tahir/Downloads/'
new_path_to_go = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/'

# First scrapping method will work

# # That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
create_folder_with_uniq_cities(FILE_DOWNLOADED_PATH, CITIES_CREATE_PATH)

send_preprocess_scraped_exel2csv_files_dataset_folder(downloaded_path, new_path_to_go)

# # # # That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# find_subcities_convert2csv_save(MAIN_FOLDER_PATH)

# # # # That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# find_subcities_preprocess_and_saveas_new_folder(MAIN_FOLDER_PATH, NEW_PATH)

# # # # That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# create_new_df_from_mean_4all_subcities(NEW_PATH) #Concat işlemi iki df için yapildi eğer daha fazla df varsa nasil yapilir öğren entegre et

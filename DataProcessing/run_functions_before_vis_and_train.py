import pandas as pd
from create_folder_for_uniq_cities import create_folder_with_uniq_cities
from create_averagedf4allcities import create_new_df_from_mean_4all_subcities
from scrapped_file_preprocessing_and_routing import send_preprocess_scraped_exel2csv_files_dataset_folder

MAIN_PATH4DATA = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset'
FILE_DOWNLOADED_PATH = '/home/tahir/Downloads/'

# First scrapping method will work

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# create_folder_with_uniq_cities(FILE_DOWNLOADED_PATH, MAIN_PATH4DATA)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
send_preprocess_scraped_exel2csv_files_dataset_folder(FILE_DOWNLOADED_PATH, MAIN_PATH4DATA)

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
create_new_df_from_mean_4all_subcities(MAIN_PATH4DATA) 

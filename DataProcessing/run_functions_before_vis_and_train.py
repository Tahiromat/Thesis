import pandas as pd
from convert_all_xlsx_files2csv import find_subcities_convert2csv_save
from preprocess_all_csv_file import find_subcities_preprocess_and_saveas_new_folder
from datasets_merging import create_new_df_from_mean_4all_subcities

MAIN_FOLDER_PATH = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/RawData'
NEW_PATH = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset'

# First scrapping method will work

# Secondly Scrapped file preprocessing method will work

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
find_subcities_convert2csv_save(MAIN_FOLDER_PATH)

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
find_subcities_preprocess_and_saveas_new_folder(MAIN_FOLDER_PATH, NEW_PATH)

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
create_new_df_from_mean_4all_subcities(NEW_PATH) #Concat işlemi iki df için yapildi eğer daha fazla df varsa nasil yapilir öğren entegre et

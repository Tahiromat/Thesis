import pandas as pd
from convert_all_xlsx_files2csv import find_subcities_convert2csv_save
from preprocess_all_csv_file import find_subcities_preprocess_and_saveas_new_folder

MAIN_FOLDER_PATH = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/RawData'
NEW_PATH = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset'

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
find_subcities_convert2csv_save(MAIN_FOLDER_PATH)

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
find_subcities_preprocess_and_saveas_new_folder(MAIN_FOLDER_PATH, NEW_PATH)


from convert_save_files import find_subcities_convert2csv_save
from get_csv_files4preprocess import find_subcities4preprocess


MAIN_FOLDER_PATH = '/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/RawData'

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Find all .xlsx files and convert them into .csv files 
find_subcities_convert2csv_save(MAIN_FOLDER_PATH)

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Find all .csv files and prepare data for processing 
find_subcities4preprocess(MAIN_FOLDER_PATH)


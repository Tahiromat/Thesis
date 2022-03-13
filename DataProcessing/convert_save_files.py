from read_and_convert_file import convert_xlsx2csv, read_excel_file
import os

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def __subfolder_convert_and_save_files(main_folder_path, city_name):

    # file_paths = []
    os.chdir(main_folder_path + '/' + city_name)

    for f in os.listdir():

        f_name, f_ext = os.path.splitext(f)
        if f_ext == '.xlsx':

            xlsx_path = main_folder_path + '/' + city_name + '/' + f_name + '.xlsx'
            # file_paths.append(xlsx_path)

            convert_xlsx2csv(read_excel_file(main_folder_path + '/' + city_name, f_name), main_folder_path + '/' + city_name, f_name)

# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def find_subcities_convert2csv_save(main_folder_path):

    for city_name in os.listdir(main_folder_path):

        __subfolder_convert_and_save_files(main_folder_path, city_name)

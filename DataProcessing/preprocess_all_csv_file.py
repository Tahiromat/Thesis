# import os 
# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# # That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def __change_dtype_utility(df, name, current_param, replaced_param):
#     return df[name].astype(str).str.replace(current_param,replaced_param, regex=True)

# # That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def __preprocess_sub_csv_file_and_send2new_directory(raw_csv_file_path, saved_file_path):
#     df = pd.read_csv(raw_csv_file_path)
#     total_column_names = df.columns
#     total_column_names = total_column_names[1:]
#     for name in total_column_names:
#         df[name] = __change_dtype_utility(df, name, '-', '0')
#         df[name] = __change_dtype_utility(df, name, '.', '')
#         df[name] = __change_dtype_utility(df, name, ',', '.')
#         df[name] = df[name].astype(float)
#     df.to_csv(saved_file_path, index=False)

# # That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def __send_files_under_subfolder(old_subfolder_path, new_subfolder_path, city_name):
#     os.chdir(old_subfolder_path + '/' + city_name)
#     for f in os.listdir():
#         f_name, f_ext = os.path.splitext(f)
#         if f_ext == '.csv':
#             csv_path = old_subfolder_path + '/' + city_name + '/' + f
#             saved_path = new_subfolder_path + '/'  + city_name + '/' + f
#             __preprocess_sub_csv_file_and_send2new_directory(csv_path, saved_path)

# # That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# def find_subcities_preprocess_and_saveas_new_folder(raw_main_folder_path, new_main_folder_path):
#     print('\n\nAll .csv files preprocessing and saving new directory......................................................... \n')
#     for city_name in os.listdir(raw_main_folder_path):
#         __send_files_under_subfolder(raw_main_folder_path, new_main_folder_path, city_name)

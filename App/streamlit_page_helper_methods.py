import os

def city_names(main_folder_path):

    city_name_list = []

    for city_name in os.listdir(main_folder_path):
        city_name_list.append(city_name)
        
    return city_name_list


# city_names(MAIN_FOLDER_PATH)

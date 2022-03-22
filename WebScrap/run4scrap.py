import helper_functions4scrap as hlp_mthds

# 1) Load page
print('\n************************************ Loadind Main Page ************************************\n')
hlp_mthds.load_main_page()

# 2) Select all cities
print('\n************************************ Selecting All(81) Cities ************************************\n')
hlp_mthds.select_all_city()

# 3) Select Station
# For that method fallow this link: https://www.youtube.com/watch?v=p9NpddaIZWs
print('\n************************************ Selecting Station For Data ************************************\n')
hlp_mthds.select_station()

# 4) Select all 7 parameters
print('\n************************************ Selecting All(7) Parameters ************************************\n')
hlp_mthds.select_seven_parameters()

# 5) Select hourly df
print('\n************************************ Selecting Hourly Data ************************************\n')
hlp_mthds.select_data_time_type()

# 6) Select start date
print('\n************************************ Selecting Start Date ************************************\n')
hlp_mthds.select_start_date()

# 7) Select end date
print('\n************************************ Selecting End Date ************************************\n')
# hlp_mthds.select_end_date()

# 8) Select inquire for df
print('\n************************************ Inquiring To Data ************************************\n')
hlp_mthds.inquire_for_data_file()

# 9) Select export data to xlsx file
print('************************************ Exporting Data To Xlsx File ************************************\n')
hlp_mthds.export_data_to_xlsx_file()

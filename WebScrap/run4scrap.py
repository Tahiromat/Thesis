from ast import While
import constants as const
from selenium import webdriver
import helper_functions4scrap as hlp_mthds
from webdriver_manager.chrome import ChromeDriverManager

DRIVER = webdriver.Chrome(ChromeDriverManager().install())
DATA_START_DATE = '26.03.2022 00:00'

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

while True:
    for STATION_NAME in const.STATION_LIST:
        print(f'Downloading {STATION_NAME} data')
        hlp_mthds.run_all_scrap_help_functions(DRIVER, STATION_NAME, DATA_START_DATE)
        print(f'{STATION_NAME} data succesfully downloaded\n')



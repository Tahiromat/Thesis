import constants as const
from selenium import webdriver
import helper_functions4scrap as hlp_mthds
from webdriver_manager.chrome import ChromeDriverManager

DRIVER = webdriver.Chrome(ChromeDriverManager().install())

for STATION_NAME in const.STATION_LIST:
    hlp_mthds.run_all_scrap_help_functions(DRIVER, STATION_NAME, '22.03.2022 16:00')


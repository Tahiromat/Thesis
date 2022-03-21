####################### DO NOT CHANGE THAT METHODS ####################### 

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
import constants as const
driver = webdriver.Chrome(ChromeDriverManager().install())

def load_main_page():
    driver.maximize_window()
    driver.get(const.BASE_URL)
    time.sleep(5)
    pass

def select_all_city():
    # select_all_cities_button = driver.find_element(By.XPATH, const.SELECT_ALL_CITIES_PATH)
    # select_all_cities_button.click()
    # time.sleep(5)
    pass

def select_seven_parameters():
    # select_all_parameters4df = driver.find_element(By.XPATH, const.SELECT_ALL_PARAMETERS_FOR_DF_PATH)
    # select_all_parameters4df.click()
    # time.sleep(5)
    pass

def select_station():
    station = driver.find_element(By.ID, const.STATION_NAMES_PATH)
    stationDD = Select(station)
    stationDD.select_by_index(3)
    time.sleep(5)
    # pass

def select_data_time_type():
    # hourly_df = driver.find_element(By.XPATH, const.HOURLY_DF_PATH)
    # hourly_df.click()
    # time.sleep(5)
    pass

def select_start_date():
    pass

def select_end_date():
    pass

def inquire_for_data_file():
    # inquire_df = driver.find_element(By.XPATH, const.INQUIRE_FOR_DF_PATH)
    # inquire_df.click()
    # time.sleep(5)
    pass

def export_data_to_xlsx_file():
    # export_df = driver.find_element(By.XPATH, const.EXPORT_DF_TO_XLSX_PATH)
    # export_df.click()
    # time.sleep(5)
    pass

def replace_filename_with_selected_station_name():
    pass

def send_xlsx_file2related_folder_under_RawData():
    pass

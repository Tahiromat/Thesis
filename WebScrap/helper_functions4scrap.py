####################### DO NOT CHANGE THAT METHODS ####################### 

import time
from datetime import date
import constants as const
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(ChromeDriverManager().install())

def load_main_page():
    driver.maximize_window()
    driver.get(const.BASE_URL)
    time.sleep(3)

def select_all_city():
    select_all_cities_button = driver.find_element(By.XPATH, const.SELECT_ALL_CITIES_PATH)
    select_all_cities_button.click()
    time.sleep(3)

def select_seven_parameters():
    select_all_parameters4df = driver.find_element(By.XPATH, const.SELECT_ALL_PARAMETERS_FOR_DF_PATH)
    select_all_parameters4df.click()
    time.sleep(3)

def select_station():
    dropdown_button = driver.find_element(By.XPATH, const.SELECT_STATION_DROPDOWN_BUTTON_PATH)
    driver.execute_script("arguments[0].click();", dropdown_button)
    time.sleep(2)
    station = driver.find_element(By.XPATH, const.STATION_NAME_PATH)
    station.send_keys('Adana - Valilik')
    time.sleep(3)

def select_data_time_type():
    hourly_df = driver.find_element(By.XPATH, const.HOURLY_DF_PATH)
    hourly_df.click()
    time.sleep(3)

def select_start_date():
    select_start_date = driver.find_element(By.XPATH, const.START_DATE_PATH)
    select_start_date.clear()
    select_start_date.send_keys('21.02.2022 16:00')
    select_start_date.click()
    time.sleep(3)

def select_end_date():
    select_end_date = driver.find_element(By.XPATH, const.END_DATE_PATH)
    select_end_date.clear()
    last_day = str(date.today().strftime("%d/%m/%Y"))
    last_day = last_day.replace('/', '.')
    select_end_date.send_keys(last_day)
    select_end_date.click()
    time.sleep(3)

def inquire_for_data_file():
    inquire_df = driver.find_element(By.XPATH, const.INQUIRE_FOR_DF_PATH)
    inquire_df.click()
    time.sleep(5)

def export_data_to_xlsx_file():
    # export_df_button = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, const.EXPORT_DF_TO_XLSX_PATH))).click()
    export_df_button = driver.find_element(By.XPATH, const.EXPORT_DF_TO_XLSX_PATH)
    export_df_button.click()
    time.sleep(30)

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

    dropdown_button = driver.find_element(By.XPATH, "//*[@id='StationDataDownloadForm']/fieldset[1]/div[1]/div[1]/div[1]/div[5]/div/div/span[1]/span/span[2]/span")
    driver.execute_script("arguments[0].click();", dropdown_button)
    time.sleep(1)

    stations = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, "StationIds_0dc340f9_listbox")))
    station = Select(stations)
    station.select_by_index(5)
    time.sleep(3)

def select_data_time_type():
    hourly_df = driver.find_element(By.XPATH, const.HOURLY_DF_PATH)
    hourly_df.click()
    time.sleep(3)

def select_start_date():
    # Start date will be last date of the fifrst column date of old dataset
    select_start_date = driver.find_element(By.XPATH, const.START_DATE_PATH)
    select_start_date.clear()
    select_start_date.send_keys('21.02.2021 16:00')
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
    time.sleep(3)

def export_data_to_xlsx_file():
    export_df = driver.find_element(By.XPATH, const.EXPORT_DF_TO_XLSX_PATH)
    export_df.click()
    time.sleep(3)

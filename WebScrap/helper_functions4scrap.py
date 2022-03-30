import time
import constants as const
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def run_all_scrap_help_functions(DRIVER ,STATION_NAME, START_DATE):
    # Load page
    DRIVER.maximize_window()
    DRIVER.get(const.BASE_URL)
    time.sleep(2)

    # Select all cities
    select_all_cities_button = DRIVER.find_element(By.XPATH, const.SELECT_ALL_CITIES_PATH)
    select_all_cities_button.click()
    time.sleep(2)

    # Select Station
    dropdown_button = DRIVER.find_element(By.XPATH, const.SELECT_STATION_DROPDOWN_BUTTON_PATH)
    dropdown_button.click()
    time.sleep(2)
    station = DRIVER.find_element(By.XPATH, const.STATION_NAME_PATH)
    station.send_keys(STATION_NAME)
    time.sleep(2)

    # Select all 7 parameters
    select_all_parameters4df = DRIVER.find_element(By.XPATH, const.SELECT_ALL_PARAMETERS_FOR_DF_PATH)
    select_all_parameters4df.click()
    time.sleep(2)

    # Select hourly df
    hourly_df = DRIVER.find_element(By.XPATH, const.HOURLY_DF_PATH)
    hourly_df.click()
    time.sleep(2)

    # Select start date
    select_start_date = DRIVER.find_element(By.XPATH, const.START_DATE_PATH)
    select_start_date.clear()
    select_start_date.send_keys(START_DATE)
    select_start_date.click()
    time.sleep(2)

    # Select inquire for df
    inquire_df = DRIVER.find_element(By.XPATH, const.INQUIRE_FOR_DF_PATH)
    inquire_df.click()
    time.sleep(3)

    # Select export data to xlsx file
    export_df_button = WebDriverWait(DRIVER, 6).until(EC.presence_of_element_located((By.XPATH, const.EXPORT_DF_TO_XLSX_PATH)))
    time.sleep(1)
    export_df_button.click()
    time.sleep(3)

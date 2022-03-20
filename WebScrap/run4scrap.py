
####################### DO NOT CHANGE THAT METHODS ####################### 

import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import constants as const
import helper_functions4scrap as hlp_mthds

driver = webdriver.Chrome(ChromeDriverManager().install())


def load_main_page():
    # Ana sayfayı yükle 
    driver.maximize_window()
    driver.get(const.BASE_URL)

def select_city():
    # 81 ilin hepsini işaretle
    load_main_page()
    time.sleep(5)
    pass

select_city()

# def select_station():
#     # İstasyon seç 
#     pass

# def select_seven_parameters():
#     # Dataset için gerekli 7 parametreyi seç
#     pass

# def select_data_time_type():
#     # Saatlik data olacak şekilde seçim yap
#     pass

# def select_start_date():
#     # Başlangıç tarihi seç
#     pass

# def select_end_date():
#     # Bitiş tarihi seç
#     pass

# def inquire_for_data_file():
#     # Seçimler doğrultusunda veri setini sorgula
#     pass

# def export_data_to_xlsx_file():
#     # Excel dosyasını indirilenler kalsörünün altına kaydet
#     pass

# def replace_filename_with_selected_station_name():
#     # İndirilen dosyaya indirilen istasyon adını ver
#     pass

# def send_xlsx_file2related_folder_under_RawData():
#     # Dosyayı RawData klasörünün altında ilgili şehre kaydet
#     pass

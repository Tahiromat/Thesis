import os
import time
import pandas as pd
import warnings
warnings.simplefilter("ignore")

def preprocess_scraped_exel_file(downloaded_path, new_path_to_go, file):
    df = pd.read_excel(downloaded_path + '/' + file)
    file_name = df.columns[1]
    file_name = file_name.replace(' ', '')
    file_name = file_name.replace('-', '')
    file_name = file_name.replace('/', '')
    real_columns = df.loc[0]
    df.columns = real_columns
    df.drop(labels=0, axis=0, inplace=True)
    df.columns=df.columns.astype(str)
    df.rename(columns={'NaT':'Tarih'}, inplace=True)
    df.to_csv(new_path_to_go + file_name + '.csv', index=False)

def send_xlsx_file(file):
    # File will be send to raw data
    pass

def send_xlsx_file2related_folder_under_RawData(downloaded_path, new_path_to_go):
    os.chdir(downloaded_path)
    for file in os.listdir():
        if file.startswith('Veri Detayları') and file.endswith('.xlsx'):
            preprocess_scraped_exel_file(downloaded_path, new_path_to_go, file)
            time.sleep(1)
        else:
            os.remove(file)
            time.sleep(1)

downloaded_path = '/home/tahir/Downloads/'
new_path_to_go = '/home/tahir/Downloads/'

send_xlsx_file2related_folder_under_RawData(downloaded_path, new_path_to_go)


# For copying the files --> https://stackoverflow.com/questions/3397752/copy-multiple-files-in-python
# For create new folder and past copied files --> https://www.codegrepper.com/code-examples/python/how+to+create+a+new+folder+in+python
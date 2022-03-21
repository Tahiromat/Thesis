import pandas as pd
import warnings
warnings.simplefilter("ignore")

def send_xlsx_file2related_folder_under_RawData(downloaded_path,file_old_name, new_path_to_go):
    df = pd.read_excel('/home/tahir/Downloads/Veri Detayları3_20_2022, 3_18_25 PM.xlsx')
    file_name = df.columns[1]
    real_columns = df.loc[0]
    df.columns = real_columns
    df.drop(labels=0, axis=0, inplace=True)
    df.columns=df.columns.astype(str)
    df.rename(columns={'NaT':'Tarih'}, inplace=True)
    df.to_csv('/home/tahir/Downloads/' + file_name + '.csv', index=False)


downloaded_path = '/home/tahir/Downloads/'
file_old_name = 'Veri Detayları3_20_2022, 3_18_25 PM.xlsx'
new_path_to_go = '/home/tahir/Downloads/'

send_xlsx_file2related_folder_under_RawData(downloaded_path, file_old_name, new_path_to_go)
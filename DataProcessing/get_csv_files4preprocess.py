import os 
from preprocess_file import preprocess_sub_csv_file

# import seaborn as sns
# import matplotlib.pyplot as plt

def __subfolder_preprocess(main_folder_path, city_name):

    os.chdir(main_folder_path + '/' + city_name)

    for f in os.listdir():

        f_name, f_ext = os.path.splitext(f)
        if f_ext == '.csv':

            # print(f)

            csv_path = main_folder_path + '/' + city_name + '/' + f
            # file_paths.append(csv_path)
            print(csv_path)

            print(f'\n{f_name} DATASET LOADING ...................\n\n')
            df = preprocess_sub_csv_file(csv_path)
            print(f'\n\n{df.columns}\n\n')
            
            '''# Tüm dflerdeki colon sayısı eşit olmalıdır bunu da kontrolünü grafiklerini çizdirerek yapmalısın.
            # Her bir colon name için tüm dflerin grafiğini çizdir. Eksik kolonları oluştur ve değerlerini sıfırlardan oluştur.
            sns.scatterplot(data= df, x='Tarih', y='PM 2.5 ( µg/m3 )')
            plt.title(f_name)
            plt.show()'''
            # Burada değişikler df de kalıcı olarak kaydedilmelidir.


# That Method Work Clearly !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! DO NOT CHANGE THAT METHOD !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def find_subcities4preprocess(main_folder_path):

    for city_name in os.listdir(main_folder_path):
        print(city_name)

        __subfolder_preprocess(main_folder_path, city_name)


# find_subcities4preprocess(MAIN_FOLDER_PATH)
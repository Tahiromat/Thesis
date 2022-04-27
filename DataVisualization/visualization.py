"""
    * Burada her bir görselleştirme tekniği için ayrı fonsiyon tanımlanacak(görselleştirme tipi (line, scatter, vs))
    * Fonksiyonlar app dosyasına import edilecek ve app dosyasında dataların path ini tutan bir liste olacak. 
    * Görselleştirme sayfasında görselleştirme türü vs seçildikten sonra data pathı verilerek istenilen bölgenin istenilde tipte 
        görselleştirmesi sağlanacak.
    * Visulization types :
        * Use comparative visualization like whats the effect of the any column on the total dirty quality (add hue value)
        * line plot
        * scatter plot 

    
"""



import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('/home/tahir/Documents/DataScience/HavaKalitesiAnomaliTespiti/Dataset/İstanbul/İstanbulAverageDF.csv')
print(df.columns)
df = df[:-1]
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S.%f')



name_list = df.columns[1:]
for name in name_list:
    sns.lineplot(data=df, x='Date', y=name)
    plt.title(name)
    # plt.grid()
    plt.show()



def visualize_PM10():
    sns.lineplot(data=df, x='Date', y='PM10 ( µg/m3 )')
    plt.title('PM10 ( µg/m3 )')
    plt.show()

def visualize_PM_25():
    sns.lineplot(data=df, x='Date', y='PM 2.5 ( µg/m3 )')
    plt.title('PM 2.5 ( µg/m3 )')
    plt.show()

def visualize_SO2():
    sns.lineplot(data=df, x='Date', y='SO2 ( µg/m3 )')
    plt.title('SO2 ( µg/m3 )')
    plt.show()

def visualize_CO():
    sns.lineplot(data=df, x='Date', y='CO ( µg/m3 )')
    plt.title('CO ( µg/m3 )')
    plt.show()

def visualize_NO2():
    sns.lineplot(data=df, x='Date', y='NO2 ( µg/m3 )')
    plt.title('NO2 ( µg/m3 )')
    plt.show()

def visualize_NOX():
    sns.lineplot(data=df, x='Date', y='NOX ( µg/m3 )')
    plt.title('NOX ( µg/m3 )')
    plt.show()

def visualize_O3():
    sns.lineplot(data=df, x='Date', y='O3 ( µg/m3 )')
    plt.title('O3 ( µg/m3 )')
    plt.show()




visualize_PM10()
visualize_PM_25()
visualize_SO2()
visualize_CO()
visualize_NO2()
visualize_NOX()
visualize_O3()




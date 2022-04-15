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
df = df[:-1]
df['Date'] = pd.to_datetime(df['Date'], format='%Y-%m-%d %H:%M:%S.%f')

name_list = df.columns[1:]
for name in name_list:
    sns.lineplot(data=df, x='Date', y=name)
    plt.title(name)
    plt.grid()
    plt.show()



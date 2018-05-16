import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# os.chdir("C:/Users/AHMET.TUNCEL/Desktop/MEF Yüksek Lisans/BDA 502-01 Introduction to Machine Learning/ML_Project")

os.chdir("H:/Yuksek Lisans ML Proje ve Verileri")



print("Current Working Directory " , os.getcwd())

# Data Load

urunetiketdf = pd.read_csv('UrunEtiket.csv')


urunetiketdf[['HaftaAraligi','UrunDurum']].isnull().values.any()


urunetiketdf.iloc[:,2:].isnull().values.any()


print(urunetiketdf.columns)

print(urunetiketdf.head())

print(urunetiketdf.shape)



# Update to nan values		
# kriterrangedf = kriterrangedf.fillna(999)

kriterrangedf.iloc[:,4:] = kriterrangedf.iloc[:,4:].astype('int64')

kriterrangedf.head()

kriterrangedf[(kriterrangedf.MerchMarkaYasGrupRef == 2) & (kriterrangedf.KlasmanGrupRef == 63 )].count()




print(kriterrangedf['HaftaAraligi'].unique())

Kriterrangedf201701_201705 = kriterrangedf[kriterrangedf.HaftaAraligi == '201701-201705']

CountUrunDurum = Kriterrangedf201701_201705['UrunDurum'].value_counts()

type(CountUrunDurum)



CountUrunDurumdf = pd.DataFrame(CountUrunDurum)


ax = CountUrunDurumdf.plot(kind='bar',figsize=(15,10), fontsize=12)
ax.set_xlabel('dim_contact_channel',fontsize=12)
ax.set_ylabel('channel',fontsize=12)
plt.show()



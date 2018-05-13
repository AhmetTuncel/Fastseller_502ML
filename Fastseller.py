import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

os.chdir("C:/Users/AHMET.TUNCEL/Desktop/MEF Yüksek Lisans/BDA 502-01 Introduction to Machine Learning/ML_Project")
print("Current Working Directory " , os.getcwd())

# Data Load
kriterrangedf = pd.read_csv('KriterRange.csv')

# Data description

print(kriterrangedf.head())

print(kriterrangedf.shape)

print(kriterrangedf.columns)

print(kriterrangedf.info())

# Dimension variable
print(kriterrangedf[['HaftaAraligi', 'MerchMarkaYasGrupRef', 'KlasmanGrupRef', 'UrunDurum']].info())



# Find max value for update to NaN values 
def findmaxrangevalue():
    
    rangelist = []
    for i in range(4,221):  
        a = kriterrangedf.iloc[:,i].max()
        rangelist.append(a)
    return max(rangelist)     

print(findmaxrangevalue())


# kriterrangedf.describe()

# kriterrangedf.describe(include=['object', 'bool'])

# Check for nan values.
kriterrangedf[['HaftaAraligi', 'MerchMarkaYasGrupRef', 'KlasmanGrupRef', 'UrunDurum']].isnull().values.any()

kriterrangedf.iloc[:,4:].isnull().values.any()

# Update to nan values		
kriterrangedf = kriterrangedf.fillna(999)

kriterrangedf.iloc[:,4:] = kriterrangedf.iloc[:,4:].astype('int64')

kriterrangedf.head()



kriterrangedf.groupby('HaftaAraligi').agg('count').plot(kind='bar')



print(kriterrangedf['HaftaAraligi'].unique())

Kriterrangedf201701_201705 = kriterrangedf[kriterrangedf.HaftaAraligi == '201701-201705']

CountUrunDurum = Kriterrangedf201701_201705['UrunDurum'].value_counts()


Kriterrangedf201701_201705.groupby('UrunDurum').agg('count')[['Survived', 'Died']].plot(kind='bar')




CountUrunDurumdf = pd.DataFrame(CountUrunDurum)

CountUrunDurumdf.columns = ['Count']

print(CountUrunDurumdf)


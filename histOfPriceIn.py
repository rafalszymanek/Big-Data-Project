import json
import statistics
from matplotlib import pyplot as plt
import numpy as np
import seaborn as sns

data = {}
data["Celowniki, lunety"] = [] 
data["Części ASG"] = [] 
data["Karabinki szturmowe"] = [] 
data["Karabinki maszynowe"] = [] 
data["Karabiny snajperskie"] = [] 
data["Kulki ASG"] = [] 
data["Magazynki"] = []
data["Oporządzenie taktyczne"] = [] 
data["Osprzęt ASG"] = [] 
data["Pistolety i rewolwery"] = [] 
data["Pistolety maszynowe"] = [] 
data["Strzelby"] = [] 
data["Pozostałe"] = [] 

with open('allProductsInCategories.json') as json_file:
    jsonData = json.load(json_file)

    for oneCategory in data:
        for p in jsonData[oneCategory]:
            data[oneCategory].append({
                'nazwa': p['nazwa'],
                'cena': p['cena'],
                'cena_z_dostawa': p['cena_z_dostawa'],
                'licytacja': p['licytacja'],
                'ile_osob_kupilo': p['ile_osob_kupilo'],
                'allegro_smart': p['allegro_smart'],
                'ssprzedawca': p['ssprzedawca'],
                'cena': p['cena'],
                'stan': p['stan']
            })

medianArray = []

oneCategoryPrices = []
for i in data["Karabinki szturmowe"]:
    arrPrice = []
    for y in i['cena'] :
        if y.isdigit():
            arrPrice.append(y)
    oneCategoryPrices.append(float(''.join(arrPrice))/100)

lowQuantile= np.quantile(oneCategoryPrices, 0.05)
highQuantile = np.quantile(oneCategoryPrices, 0.95)
afterQuantile = []
for price in oneCategoryPrices:
    if lowQuantile <= price <= highQuantile:
        afterQuantile.append(price)

# print(afterQuantile)
f1 = plt.figure(1)
plt.tight_layout
sns.distplot(afterQuantile)
plt.axvline(statistics.median(afterQuantile), color='#fc4f30', label='Mediana')
plt.axvline(statistics.mean(afterQuantile), color='#11ff11', label='Średnia arytm.')
plt.legend()

plt.title('Rozkład cen kategorii "Karabiny szturmowe"')
plt.xlabel('Cena [zł]')

# f2 = plt.figure(2)
# plt.style.use('fivethirtyeight')
# bin = np.arange(200, 2000, 50)

# plt.hist(afterQuantile, bins = bin, density=True)
# 


plt.show()
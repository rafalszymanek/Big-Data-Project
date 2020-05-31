import json
import statistics
from matplotlib import pyplot as plt
import numpy as np

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

for oneCategory in data:
    oneCategoryPrices = []
    for i in data[oneCategory]:
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

    medianArray.append(round(statistics.median(afterQuantile), 2))

    


print(medianArray)


objects = ["Celowniki, lunety", 
"Części ASG",
"Karabinki szturmowe",
"Karabinki maszynowe",
"Karabiny snajperskie",
"Kulki ASG",
"Magazynki",
"Oporządzenie taktyczne",
"Osprzęt ASG",
"Pistolety i rewolwery",
"Pistolety maszynowe" ,
"Strzelby" ,
"Pozostałe"
]

y_pos = np.arange(len(objects))
performance = medianArray

plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Cena [zł]')
plt.title('Mediana cen w rozrónieniu na kategorie', fontsize=14, fontweight='bold')

for i, v in enumerate(performance):
    plt.text(v + 5, i - 0.15, str(v), color='blue', fontsize=9, fontweight='bold')

plt.show()


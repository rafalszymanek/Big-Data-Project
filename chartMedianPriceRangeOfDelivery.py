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


arrayDeliveryCost = []

for oneCategory in data:

    for product in data[oneCategory]:
        arrPrice = []
        for y in product['cena'] :
            if y.isdigit():
                arrPrice.append(y)
        productPrice = (float(''.join(arrPrice))/100)

        arrDelivery = []
        if type(product['cena_z_dostawa']) == int:
            break
        else:
            for y in product['cena_z_dostawa'] :
                if y.isdigit():
                    arrDelivery.append(y)
            if arrDelivery != []:
                priceWithDelivery = (float(''.join(arrDelivery))/100)
            
                deliveryPrice = priceWithDelivery-productPrice
                if deliveryPrice < 300:
                    arrayDeliveryCost.append(deliveryPrice)


print(sorted(arrayDeliveryCost))
plt.boxplot(arrayDeliveryCost)

plt.title('Rozkład kosztów dostawy"')
plt.ylabel('Cena [zł]')

plt.tight_layout
plt.show()
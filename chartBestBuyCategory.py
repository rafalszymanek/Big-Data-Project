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

totalBuysInCategory = []

for oneCategory in data:
    oneCategoryBuys = 0
    for product in data[oneCategory]:
        num = []
        if product['ile_osob_kupilo'] != False:
            for y in product['ile_osob_kupilo'] :
                if y.isdigit():
                    num.append(y)
            if num !=[]:
                oneCategoryBuys += (int(''.join(num)))
            
    totalBuysInCategory.append(oneCategoryBuys)

print(totalBuysInCategory)

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
performance = totalBuysInCategory

plt.barh(y_pos, performance, align='center', alpha=0.5)
plt.yticks(y_pos, objects)
plt.xlabel('Kupione sztuki')
plt.title('Najczęściej kupowane kategorie ASG', fontsize=14, fontweight='bold')

for i, v in enumerate(performance):
    plt.text(v + 5, i - 0.15, str(v), color='blue', fontsize=9, fontweight='bold')

plt.show()

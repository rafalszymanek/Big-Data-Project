import statistics
from matplotlib import pyplot as plt
import json
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
                'stan': p['stan']
            })

medianArrayNew = []
medianArrayUsed = []

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

for oneCategory in data:
    oneCategoryPricesNew = []
    oneCategoryPricesUsed = []
    for i in data[oneCategory]:
        arrPrice = []
        for y in i['cena']:
            if y.isdigit():
                arrPrice.append(y)
        if i['stan'] == "Nowy": oneCategoryPricesNew.append(float(''.join(arrPrice))/100)
        else: oneCategoryPricesUsed.append(float(''.join(arrPrice))/100)

    lowQuantileNew = np.quantile(oneCategoryPricesNew, 0.05)
    highQuantileNew = np.quantile(oneCategoryPricesNew, 0.95)
    afterQuantileNew = []

    lowQuantileUsed = np.quantile(oneCategoryPricesUsed, 0.05)
    highQuantileUsed = np.quantile(oneCategoryPricesUsed, 0.95)
    afterQuantileUsed = []

    for price in oneCategoryPricesNew:
        if lowQuantileNew <= price <= highQuantileNew:
            afterQuantileNew.append(price)

    for price in oneCategoryPricesUsed:
        if lowQuantileUsed <= price <= highQuantileUsed:
            afterQuantileUsed.append(price)

    medianArrayNew.append(round(statistics.median(afterQuantileNew), 2))
    medianArrayUsed.append(round(statistics.median(afterQuantileUsed), 2))

medianArrayNew1 = []
medianArrayNew2 = []
medianArrayNew3 = []
medianArrayNew4 = []

for i in range(0,len(medianArrayNew)):
    if i < 4: medianArrayNew1.append(medianArrayNew[i])
    elif i < 8: medianArrayNew2.append(medianArrayNew[i])
    elif i < 12: medianArrayNew3.append(medianArrayNew[i])
    else: medianArrayNew4.append(medianArrayNew[i])

medianArrayUsed1 = []
medianArrayUsed2 = []
medianArrayUsed3 = []
medianArrayUsed4 = []

for i in range(0,len(medianArrayUsed)):
    if i < 4: medianArrayUsed1.append(medianArrayUsed[i])
    elif i < 8: medianArrayUsed2.append(medianArrayUsed[i])
    elif i < 12: medianArrayUsed3.append(medianArrayUsed[i])
    else: medianArrayUsed4.append(medianArrayUsed[i])

objects1 = []
objects2 = []
objects3 = []
objects4 = []

for i in range(0,len(objects)):
    if i < 4: objects1.append(objects[i])
    elif i < 8: objects2.append(objects[i])
    elif i < 12: objects3.append(objects[i])
    else: objects4.append(objects[i])

#1 wykres
def wykres1():
    fig, ax = plt.subplots()
    index = np.arange(4)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, medianArrayNew1, bar_width,
    alpha=opacity,
    color='b',
    label='Nowe')

    rects2 = plt.bar(index + bar_width, medianArrayUsed1, bar_width,
    alpha=opacity,
    color='g',
    label='Używane')

    plt.xlabel('Kategorie')
    plt.ylabel('Ceny')
    plt.title('Porównanie cen dla poszczególnych kategoriach')
    plt.xticks(index + bar_width, objects1)
    plt.legend()

    plt.tight_layout()
    plt.show()

#2 wykres
def wykres2():
    fig, ax = plt.subplots()
    index = np.arange(4)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, medianArrayNew2, bar_width,
    alpha=opacity,
    color='b',
    label='Nowe')

    rects2 = plt.bar(index + bar_width, medianArrayUsed2, bar_width,
    alpha=opacity,
    color='g',
    label='Używane')

    plt.xlabel('Kategorie')
    plt.ylabel('Ceny')
    plt.title('Porównanie cen dla poszczególnych kategoriach')
    plt.xticks(index + bar_width, objects2)
    plt.legend()

    plt.tight_layout()
    plt.show()

#3 wykres
def wykres3():
    fig, ax = plt.subplots()
    index = np.arange(4)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, medianArrayNew3, bar_width,
    alpha=opacity,
    color='b',
    label='Nowe')

    rects2 = plt.bar(index + bar_width, medianArrayUsed3, bar_width,
    alpha=opacity,
    color='g',
    label='Używane')

    plt.xlabel('Kategorie')
    plt.ylabel('Ceny')
    plt.title('Porównanie cen dla poszczególnych kategoriach')
    plt.xticks(index + bar_width, objects3)
    plt.legend()

    plt.tight_layout()
    plt.show()

#4 wykres
def wykres4():
    fig, ax = plt.subplots()
    index = np.arange(1)
    bar_width = 0.35
    opacity = 0.8

    rects1 = plt.bar(index, medianArrayNew4, bar_width,
    alpha=opacity,
    color='b',
    label='Nowe')

    rects2 = plt.bar(index + bar_width, medianArrayUsed4, bar_width,
    alpha=opacity,
    color='g',
    label='Używane')

    plt.xlabel('Kategorie')
    plt.ylabel('Ceny')
    plt.title('Porównanie cen dla poszczególnych kategoriach')
    plt.xticks(index + bar_width, objects4)
    plt.legend()

    plt.tight_layout()
    plt.show()

wykres1()
wykres2()
wykres3()
wykres4()
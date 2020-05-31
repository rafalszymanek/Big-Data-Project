from matplotlib import pyplot as plt
import json

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

#####################################################################
#####################################################################

FreeDelivery_On = 0
FreeDelivery_Off = 0

for oneCategory in data:
    for product in data[oneCategory]:
        if product['cena_z_dostawa'] == "darmowa dostawa": FreeDelivery_On+=1
        else: FreeDelivery_Off+=1

allegro_smart_list = [FreeDelivery_On, FreeDelivery_Off]
allegro_smart_labels = ["Darmowa dostawa", "brak"]

fig1, ax1 = plt.subplots()
patches = ax1.pie(allegro_smart_list, labels=allegro_smart_labels, radius=1, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
fig1.suptitle('Ilosc darmowych dostaw', fontsize=14, fontweight='bold')
ttl = ax1.title
ttl.set_position([.5, 1.05])
plt.show()
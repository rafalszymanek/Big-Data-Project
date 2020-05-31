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

ssprzedawca_ON = 0
ssprzedawca_OFF = 0

for oneCategory in data:
    for product in data[oneCategory]:
        if product['ssprzedawca'] == True: ssprzedawca_ON+=1
        else: ssprzedawca_OFF+=1

allegro_smart_list = [ssprzedawca_ON, ssprzedawca_OFF]
allegro_smart_labels = ["Super sprzedawca", "Inni"]

fig1, ax1 = plt.subplots()
patches = ax1.pie(allegro_smart_list, labels=allegro_smart_labels, radius=1, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
fig1.suptitle('Porównanie Super sprzedawców', fontsize=14, fontweight='bold')
ttl = ax1.title
ttl.set_position([.5, 1.05])
plt.show()
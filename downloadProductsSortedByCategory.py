import requests
from bs4 import BeautifulSoup
import json

url = "https://allegro.pl/kategoria/asg-celowniki-lunety-253884?bmatch=al-product-eyesa2-mentat-spo-1-4-0528"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

minimum = 0
maximum = 10
number_of_sites = 1
miasto = "Wroclaw"
wanna_check_for_prices = 0
wanna_check_with_city = 0

price_from = "price_from=" + str(minimum) + "&"
price_to = "price_to=" + str(maximum) + "&"
page_num = "p="
city = "&city="

check_if_duplicate = []

# JSON structure
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

html_section = soup.find('span', class_='_1h7wt _1fkm6 _g1gnj _3db39_3i0GV _3db39_XEsAE')
num_of_pages = html_section.text.strip()
for i in range(int(num_of_pages)):
    base_url = "https://allegro.pl/kategoria/asg-celowniki-lunety-253884?bmatch=al-product-eyesa2-mentat-spo-1-4-0528"
    page = requests.get(base_url+"&p="+str(i+1))
    print(url+"&p="+str(i+1))
    soup = BeautifulSoup(page.content, 'html.parser')

    for post in soup.findAll("div", {"class":"_9c44d_1V-js"}):
        nazwa = post.findAll("h2", {"class":"_9c44d_LUA1k"})[0].text
        if not nazwa in check_if_duplicate:
            check_if_duplicate.append(nazwa)
            link0 = post.findAll("h2", {"class":"_9c44d_LUA1k"})[0]
            link1 = [a['href'] for a in link0('a', href=True) if a.text]
            link=link1[0]
            cena = post.findAll("span", {"class":"_9c44d_1zemI"})[0].text
            dane0 = post.findAll("div", {"class":"_9c44d_Pjt1U"})[0]
            ssprzedawca = post.findAll("div", {"class":"_9c44d_tND42"})
            licytacja = post.findAll("div", {"class":"_9c44d_3kZXX"})
            cena_z_dostawa = ""
            cena_z_dostawa0 = post.findAll("div", {"class":"_9c44d_21XN-"})
            for item in cena_z_dostawa0:
                item = str(item)
                item = item.replace("<div class=\"_9c44d_21XN-\"><i>", "")
                item = item.replace("</i></div>", "")
                item = item.replace("<div class=\"_9c44d_21XN- _9c44d_2M5cs\"><i>", "")
                item = item.replace("<i>", "")
                item = item.replace("</i>", "")
                cena_z_dostawa = item
            AllegroSMART = post.findAll("span", {"class":"_9c44d_1H9bh"})
            ile_osob_kupilo = post.findAll("span", {"class":"_9c44d_2o04k"})[0].text
            dane10 = []
            dane1 = dane0.find_all("dt")
            for item in dane1:
                item = str(item)
                item = item.replace("<dt>", "")
                item = item.replace("</dt>", "")
                dane10.append(item)
            dane20 = []
            dane2 = dane0.find_all("dd")
            for item in dane2:
                item = str(item)
                item = item.replace("<dd>", "")
                item = item.replace("<dd class=\"_9c44d_znb10\">", "")
                item = item.replace("</dd>", "")
                dane20.append(item)

            if cena_z_dostawa:
                cena_z_dostawa = cena_z_dostawa
            else:
                cena_z_dostawa = 0

            if licytacja:
                licytacja = True
            else:
                licytacja = False
            
            if ile_osob_kupilo:
                ile_osob_kupilo = ile_osob_kupilo
            else:
                ile_osob_kupilo = False

            if AllegroSMART:
                AllegroSMART = True
            else:
                AllegroSMART = False

            if ssprzedawca:
                ssprzedawca = True
            else:
                ssprzedawca = False

            for i in range(len(dane10)): 
                stan = dane20[i]
            

            data['Celowniki, lunety'].append({
                'nazwa': nazwa,
                'cena': cena,
                'cena_z_dostawa': cena_z_dostawa,
                'licytacja': licytacja,
                'ile_osob_kupilo': ile_osob_kupilo,
                'allegro_smart': AllegroSMART,
                'ssprzedawca': ssprzedawca,
                'cena': cena,
                'stan': stan
            })

parsed = json.loads(json.dumps(data))
    # print(type(data))
    # print(json.dumps(parsed, indent=4, sort_keys=True))
with open('allProductsInCategories.json', 'w+') as outfile:
    json.dump(parsed, outfile, indent=4, sort_keys=True)
    # print(nazwa)
    # print(cena)
    # if cena_z_dostawa:
    #     print(cena_z_dostawa)
    # if licytacja:
    #     print("LICYTACJA")
    # if ile_osob_kupilo:
    #     print(ile_osob_kupilo)
    # if AllegroSMART:
    #     print("Allegro SMART")
    # if ssprzedawca:
    #     print("Super Sprzedawca")
    # for i in range(len(dane10)): print(dane10[i] + ": " + dane20[i])
    # print(link)
    # print("\n")
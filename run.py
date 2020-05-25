from urllib.request import urlopen
from bs4 import BeautifulSoup as b

minimum = 0
maximum = 10
number_of_sites = 1
miasto = "Wroclaw"

wanna_check_for_prices = 0
wanna_check_with_city = 0

base_url = "https://allegro.pl/listing?string="
request = "ASG"
url_separator = "&bmatch=baseline-al-product-eyesa2-engag-dict43-spo-1-3-0318&"
price_from = "price_from=" + str(minimum) + "&"
price_to = "price_to=" + str(maximum) + "&"
page_num = "p="
city = "&city="

check_if_duplicate = []

for i in range(0, number_of_sites):
    url = base_url + request + url_separator
    if wanna_check_for_prices == 1:
        url = url + price_from + price_to
    url = url + page_num + str(i)
    if wanna_check_with_city == 1:
        url = url + city + miasto


    html = urlopen(url).read()
    soup = b(html, "html.parser")

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
            print(nazwa)
            print(cena)
            if cena_z_dostawa:
                print(cena_z_dostawa)
            if licytacja:
                print("LICYTACJA")
            if ile_osob_kupilo:
                print(ile_osob_kupilo)
            if AllegroSMART:
                print("Allegro SMART")
            if ssprzedawca:
                print("Super Sprzedawca")
            for i in range(len(dane10)): print(dane10[i] + ": " + dane20[i])
            print(link)
            print("\n")
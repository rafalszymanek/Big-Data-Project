import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

url = "https://allegro.pl/kategoria/militaria-asg-253882?bmatch=baseline-al-product-eyesa2-engag-dict45-spo-1-1-0528"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

step = soup.findAll("fieldset", {"class": "_1rj80 _tbx3g _g1a3g _1us1q _6kfrx _1yk0g _3e3a8_1fxS2 _3e3a8_2xlZ-"})[1]

steps = str(step)
counter = steps.count("_w7z6o _uj8z7 _3e3a8_37xqG")

dostawa1 = []
dostawa2 = []
for i in range(counter):
    post = step.findAll("a", {"class": "_w7z6o _uj8z7 _3e3a8_37xqG"})[i]
    string = post.findAll("span")
    string =str(string)
    string = string.replace("<span>", "")
    string = string.replace("</span>", "")
    string = string.replace("[", "")
    string = string.replace("]", "")
    dostawa1.append(string)
    string2 = step.findAll("span", {"class": "_1h7wt _6dhbr _1vryf _4lbi0 _1fkm6 _1yk0g _6kfrx"})[i]
    string2 =str(string2)
    string2 = string2.replace("<span class=\"_1h7wt _6dhbr _1vryf _4lbi0 _1fkm6 _1yk0g _6kfrx\">", "")
    string2 = string2.replace("</span>", "")
    dostawa2.append(string2)

fig1, ax1 = plt.subplots()
patches = ax1.pie(dostawa2, labels=dostawa1, radius=1, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
fig1.suptitle('Sposoby dostawy', fontsize=14, fontweight='bold')
ttl = ax1.title
ttl.set_position([.5, 1.05])
plt.show()
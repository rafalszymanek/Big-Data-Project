import requests
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

url = "https://allegro.pl/kategoria/militaria-asg-253882?bmatch=baseline-al-product-eyesa2-engag-dict45-spo-1-1-0528"

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

step = soup.findAll("fieldset", {"class": "_1rj80 _tbx3g _g1a3g _1us1q _6kfrx _1yk0g _3e3a8_1fxS2"})[3]
steps = str(step)
counter = steps.count("_w7z6o _uj8z7 _3e3a8_37xqG")

marka1 = []
marka2 = []
for i in range(counter):
    post = step.findAll("a", {"class": "_w7z6o _uj8z7 _3e3a8_37xqG"})[i]
    string = post.findAll("span")
    string =str(string)
    string = string.replace("<span>", "")
    string = string.replace("</span>", "")
    string = string.replace("[", "")
    string = string.replace("]", "")
    marka1.append(string)
    string2 = step.findAll("span", {"class": "_1h7wt _6dhbr _1vryf _4lbi0 _1fkm6 _1yk0g _6kfrx"})[i]
    string2 =str(string2)
    string2 = string2.replace("<span class=\"_1h7wt _6dhbr _1vryf _4lbi0 _1fkm6 _1yk0g _6kfrx\">", "")
    string2 = string2.replace("</span>", "")
    string2 = int(string2)
    marka2.append(string2)

inne = 0
suma = 0
for i in range(len(marka2)):
    suma+=marka2[i]
suma/=100

for i in range(len(marka2)):
    if marka2[i] < suma:
        inne+=marka2[i]
        marka1[i] = ' '
        marka2[i] = 0

marka1 = [elem for elem in marka1 if elem != ' ']
marka2 = [elem for elem in marka2 if elem != 0]

for i in range(len(marka1)):
    if marka1[i] == "inna":
        marka2[i]+=inne

fig1, ax1 = plt.subplots()
patches = ax1.pie(marka2, labels=marka1, radius=1, autopct='%1.1f%%', startangle=90)
ax1.axis('equal')
fig1.suptitle('Marki', fontsize=14, fontweight='bold')
ttl = ax1.title
ttl.set_position([.5, 1.05])
plt.show()
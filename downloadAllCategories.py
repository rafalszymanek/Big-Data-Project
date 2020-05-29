import requests
from bs4 import BeautifulSoup
import json

URL = 'https://allegro.pl/kategoria/militaria-asg-253882?bmatch=al-product-eyesa2-mentat-spo-1-4-0528'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

# Placeholder for our categories as a JSON file
data = {}
data['categories'] = []

# Download all element which start with class...
job_elems = soup.find_all('li', class_=lambda value: value and value.startswith("_1bo4a _xu6h2 _1rj80 _05b01_2Ncob"))

for job_elem in job_elems:
    title_elem = job_elem.find('a', class_='_w7z6o _uj8z7 _1h7wt _1bo4a _6kfrx')
    num_of_elem = job_elem.find('span', class_='_1y62o _05b01_3Wwyl')
    
    # If element doesn't exist go anyway
    if None in (title_elem, num_of_elem):
        continue

    # Parse text from numbers
    text_n_num = []
    text_w_num = (title_elem.text.strip())
    for i in text_w_num :
        if not i.isdigit():
            text_n_num.append(i)
    result = ''.join(text_n_num)

    data['categories'].append({
        'name': result,
        'number': num_of_elem.text.strip()
    })
 


with open('categories.json', 'w+') as outfile:
        json.dump(data, outfile)

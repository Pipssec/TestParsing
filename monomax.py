import requests
from bs4 import BeautifulSoup
import json


url = 'https://monomax.by/map'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
adress = soup.find_all('p', class_='name')
phones = soup.find_all('p', class_='phone')
name = 'Мономах'
sort=[]

for x in phones:
    if len(x.text) == 0:
        pass
    else:
        sort.append(x.text)

jsons = []
for x in range(len(adress)):
    jsons.append({
        'address': adress[x].text,
        'name': name,
        'phones': sort[x]
    })

with open("monomax_res.json", "w") as write_file:
     json.dump(jsons, write_file, indent=4, ensure_ascii=False)

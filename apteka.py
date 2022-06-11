import requests
from bs4 import BeautifulSoup
import json

url = 'https://www.ziko.pl/lokalizator/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
adress = soup.find_all('td', class_='mp-table-address')
time = soup.find_all('td', class_='mp-table-hours')
name = soup.find_all('span', class_='mp-pharmacy-head')

class pharmacy:
    def __init__(self, adres, name, phones, hours):
        self.address = adres
        self.name = name
        self.phones = phones
        self.working_hours = hours

sort=[]
for x in range(len(adress)):
    var1 = adress[x].text
    index = int(var1.find("tel."))
    adres = var1[0:int(index)].encode("ascii", errors="replace").decode('utf-8')
    phone = var1[(index+4):(index+17)]
    names = name[x].text
    hours = time[x].text
    sort.append(pharmacy(adres, names, phone, hours))
    

jsons = []
for x in range(len(sort)):
    apteka = sort[x].__dict__
    jsons.append(apteka)

with open("apteka_res.json", "w") as write_file:
    json.dump(jsons, write_file, indent=4)

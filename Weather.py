import requests
from bs4 import BeautifulSoup as bs  # parser

count = 3

url = "https://sinoptik.ua/погода-Гомель"
r = requests.get(url)
html = bs(r.content, "html.parser")

days = html.select('.tabs > .main')
print(days)

for day in days:
    dow = day.select_one('.day-link').text
    date = day.select_one('.date').text
    month = day.select_one('.month').text

    weather = day.select_one('.weatherIco')['title']
    min_temp = day.select_one('.temperature .min').text
    max_temp = day.select_one('.temperature .max').text

    print('{:11} {:2} {:8}: {:9} - {:10} ({})'.format(dow, date, month, min_temp, max_temp, weather))

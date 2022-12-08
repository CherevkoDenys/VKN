#1. Файл address.txt містить кілька адрес веб-сторінок, розділених крапкою з комою. Програма повинна 
#підрахувати кількість заголовків Н1-Н6 на цих веб-сторінках і записати результат у файл у форматі JSON. 
import requests
from bs4 import BeautifulSoup
import json

f = open("D:\\Git\\Repos\\VKN\\address.txt", "r")
pages = f.read().split(';')
res = {}
for url in pages:
    x = requests.get(url)
    soup = BeautifulSoup(x.text, 'html.parser')
    h = soup.findAll(["h1", "h2", "h3", "h4", "h5", "h6"])
    res[url] = len(h)
print(res)
with open('headers.json', 'w') as outfile:
    json.dump(res, outfile)

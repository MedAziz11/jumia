import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd

all_phones= []

for page in range(1, 3):
    Url = f"https://www.jumia.com.tn/smartphones/?page={page}"
    html = requests.get(Url)
    soup = BeautifulSoup(html.content, "html.parser")
    phones = soup.find_all('div', class_="info", href=True)
    print(phones)
    for phone in phones:
        title = phone.find("h2", class_="title").text
        name = title[0:title.find("-")]
        price = phone.find("span", class_="price-box ri").text
        price = price[0:price.find("TND")].replace("\xa0", "")
        price = price.replace(",", "")
        dict_phone = {"title" : name.replace("\xa0", ""), "price" : float(price), "Link" : phone["href"]}
        all_phones.append(dict_phone)
        sleep(2)
    
filtered = [phone for phone in all_phones if phone["price"]>500.000]
sorted_list = sorted(filtered, key=lambda k: -k['price']) 
print(sorted_list)
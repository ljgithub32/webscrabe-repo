from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://www.box.co.uk/rtx-3080-graphics-cards").text  # pulls html from webpage
# print(html_text)
soup = BeautifulSoup(html_text, "lxml")

for gpus in soup.find_all("div", class_="product-list-item"):

    item = gpus.find("div", class_="p-list-title-wrapper")
    item_name = item.h3.a.text
    prices = gpus.find("div", class_="p-list-price-wrapper")
    item_price = prices.span.text
    print(f"GPU name: {item_name}, Price: {item_price}")

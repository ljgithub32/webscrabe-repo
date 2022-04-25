from bs4 import BeautifulSoup
import requests
import csv

html_text = requests.get("https://www.box.co.uk/rtx-3080-graphics-cards").text  # pulls html from webpage

soup = BeautifulSoup(html_text, "lxml")  # creates soup object which is the html page

csv_file = open("box_3080_scrape.csv", "w")

csv_writer = csv.writer(csv_file)  # setting which file to write to

csv_writer.writerow(["Name", "Price", "Link"])  # setting up rows headers

for gpus in soup.find_all("div", class_="product-list-item"):  # deepest layer which still contains all info we want

    # looping as we want to go through each "product-list-item" on that page,

    item_name = gpus.find("div", class_="p-list-title-wrapper").h3.text  # parsing out title that is within h3 tag

    item_price = gpus.find("span", class_="pq-price").text  # parsing out price which is within a span with a class

    item_link = gpus.find("div", class_="p-list-title-wrapper").h3.a["href"]  # parsing out the link, [] picks out link

    print(f"GPU name: {item_name}, Price: {item_price}, Link: {item_link}")  # formatting our output

    print()  # spaces between our output

    csv_writer.writerow([item_name, item_price, item_link])  # adding variables to csv file (inside loop)

csv_file.close()

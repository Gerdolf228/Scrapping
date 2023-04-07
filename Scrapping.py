from bs4 import BeautifulSoup
import requests
import json

#url ="https://health-diet.ru/table_calorie/"
#
#headers = {
#    "accept": "*/*",
#    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
#}
#
#req = requests.get(url)
#src = req.text
#print(src)

with open("index.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, "lxml")
all_products_hrefs = soup.find_all(class_="mzr-tc-group-item-href")

all_categories_dict = {

}
for item in all_products_hrefs:
    item_text = item.text
    item_href = "https://health-diet.ru" + item.get("href")
    all_categories_dict[item_text] = item_href

with open("all_categories_dict.json", "w", encoding="utf-8") as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

#with open("all_categories_dict.json", "w", encoding="utf-8") as file:
#    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)


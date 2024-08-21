import random
import requests
from bs4 import BeautifulSoup
import lxml
import json
import csv
from time import sleep
from config import url, headers



response = requests.get(url=url, headers=headers)
src = response.text

with open("index.html", "w", encoding="utf-8") as file:
    file.write(src)

with open("index.html", encoding="utf-8") as file:
    src = file.read()

soup = BeautifulSoup(src, 'lxml')

all_products_links = soup.find_all(class_='mzr-tc-group-item-href')
all_categories_dict = {}

for item in all_products_links:
    item_text = item.text
    item_link = "https://health-diet.ru" + item.get('href')
    all_categories_dict[item_text] = item_link


with open("all_categories_dict.json", "w", encoding="utf-8") as file:
    json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

with open("all_categories_dict.json", encoding="utf-8") as file:
    all_categories = json.load(file)

rep = [' ', ',', '-']
count = 0
iteration_count = int(len(all_categories))-1
print(f"[INFO] Total iterations: {iteration_count}")
for category_name, category_link in all_categories.items():
    for item in rep:
        if item in category_name:
            category_name = category_name.replace(item, '_')

    response = requests.get(url=category_link, headers=headers)
    src = response.text

    with open(f"data/{count}_{category_name}.html", "w", encoding="utf-8") as file:
        file.write(src)

    with open(f"data/{count}_{category_name}.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, 'lxml')

    # checking web site
    alert_block = soup.find(class_="uk-alert-danger")

    if alert_block is not None:
        continue

    table_head = soup.find(class_="mzr-tc-group-table").find("tr").find_all("th")

    product = table_head[0].text
    calories = table_head[1].text
    proteins = table_head[2].text
    fats = table_head[3].text
    carbohydrates = table_head[4].text

    with open(f"data/{count}_{category_name}.csv", "w", newline='', encoding="utf-8-sig") as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow((
            product,
            calories,
            proteins,
            fats,
            carbohydrates
        ))

    # collecting product data
    products_data = soup.find(class_="mzr-tc-group-table").find("tbody").find_all("tr")

    products_info = []
    for item in products_data:
        product_tds = item.find_all("td")

        title = product_tds[0].find('a').text
        calories = product_tds[1].text
        proteins = product_tds[2].text
        fats = product_tds[3].text
        carbohydrates = product_tds[4].text

        products_info.append(
            {
                "Title": title,
                "Calories": calories,
                "Proteins": proteins,
                "Fats": fats,
                "Carbohydrates": carbohydrates
            }
        )

        with open(f"data/{count}_{category_name}.csv", "a", newline='', encoding="utf-8-sig") as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow((
                title,
                calories,
                proteins,
                fats,
                carbohydrates
            ))


    count += 1

    with open(f"data/{count}_{category_name}.json", "a", encoding="utf-8") as file:
        json.dump(products_info, file, indent=4, ensure_ascii=False)

    print(f"[INFO] Iteration {count}, {category_name}, recorded...")
    iteration_count -= 1

    if iteration_count == 0:
        print("[INFO] Work completed")
        break
    print(f"[INFO] Iterations left: {iteration_count}")
    sleep(random.randrange(2,4))
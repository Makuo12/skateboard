# This is a sample Python script.

import requests
from bs4 import BeautifulSoup
import json
import random

url = "https://www.skateboards.com/shop/?perpage=96&filter_manufacturer"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")

titles = soup.find_all("h2", class_="woocommerce-loop-product__title")
images = soup.find_all("img")
prices = soup.find_all("bdi")


def generate_random_value():
    return f"{random.randint(10000, 300000)}"

def get_image_index(list, index):
    if index > len(list)-1:
        return random.randint(0, len(list)-1)
    return index

data = "const products = [ "
# for index, img in enumerate(images):
#     name = img["alt"]
#     link = img["nitro-lazy-src"]
# with open(name.replace(" ", "-") + ".jpg", "wb") as f:
#     im = requests.get(link)
#     f.write(im.content)
# const products = [
# 				{ imageSrc: "images/product-3.png", title: "Nordic Chair", price: "$50.00" },
for index, img in enumerate(images):
    name = img["alt"].replace(" ", "-") + ".jpg"
    num = index > len(images)
    product_data = {
        "imageSrc": name,
        "title": titles[get_image_index(titles, index)].text,
        "price": generate_random_value()
    }
    json_string = json.dumps(product_data, indent=2)
    data += f"{json_string},"
    print(data)

data += " ]"

with open("items.txt", "w") as f:
    f.write(data)

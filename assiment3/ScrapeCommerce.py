import requests
from bs4 import BeautifulSoup
import pandas as pd

global data
data = []
col = [
    "item_image",
    "item_name",
    "item_price",
    "item_url",
    "item_sizes",
    "item_tyles",
    "item_reviews",
    "item_summary",
]


def save():
    df = pd.DataFrame(data, columns=col)
    df.to_csv("lttstore.csv",index=False)


def info(url):
    page = requests.get(url)
    content = BeautifulSoup(page.text, "lxml")
    styles = content.findAll("label", class_="SizeSwatch text-label")
    sizes = content.findAll("label", class_="SizeSwatch size-label")
    item_reviews = content.find("span", class_="jdgm-prev-badge__text").text
    item_summary = content.find("div", class_="Rte").text
    if len(styles) > 0:
        style = []
        for items in styles:
            style.append(items.text)
    else:
        style = None

    size = []
    for items in sizes:
        size.append(items.text)

    return size, style, item_reviews, item_summary


def extract(item):
    width = 700
    item_image = item.find("img")["data-src"]
    item_image = item_image.format(width=700)
    item_data = item.find("a", class_="ow")
    item_name = item_data.text
    item_price = item.find("span", class_="whole").text
    item_url = "https://www.lttstore.com/" + item_data["href"]
    item_name = item_name.strip()
    list1 = info(item_url)
    data.append(
        (
            item_image,
            item_name,
            item_price[0:-3],
            item_url,
            list1[0],
            list1[1],
            list1[2],
            list1[3],
        )
    )


url = "https://www.lttstore.com/collections/clothing"
page = requests.get(url)

products = BeautifulSoup(page.text, "lxml")
cloths = products.findAll("div", class_="ProductItem__Wrapper")

for items in cloths:
    extract(items)
save()


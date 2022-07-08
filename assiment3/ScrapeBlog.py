import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

global data
data = []
col = [
    "article_thumbnail",
    "article_url",
    "article_category",
    "article_autor_name",
    "article_autho_url",
    "ariticle_comments",
    "article_summary",
    "article_essay",
    "article_publish_date",
    "article_update_date",
]


def save():
    df = pd.DataFrame(data, columns=col)
    df.to_csv("raceblogdata.csv",index=False)


def mainblock(url):
    page = requests.get(url)
    article = BeautifulSoup(page.text, "lxml")
    article_essay = article.find("div", class_="entry-content").text
    try:
        article_publish_date = article.find("time", class_="entry-date published")[
            "datetime"
        ]
    except:
        article_publish_date = None
    try:
        article_update_date = article.find("time", class_="updated")["datetime"]
    except:
        article_update_date = None
    article_essay=article_essay.strip()
    return article_essay, article_publish_date, article_update_date


def basic_data(article):
    article_url = article.find("a", class_="post-thumbnail-homepage")["href"]
    article_thumbnail = article.find("img")["src"]
    article_category = article.find("h3", class_="subtitle").text
    article_autor = article.find("a", class_="author")
    article_autho_url = article_autor["href"]
    article_autor_name = article_autor.text
    ariticle_comments = article.find("a", class_="comments-link").text
    article_summary = article.find("p").text
    list1 = mainblock(article_url)
    data.append(
        (
            article_thumbnail,
            article_url,
            article_category,
            article_autor_name,
            article_autho_url,
            ariticle_comments,
            article_summary,
            list1[0],
            list1[1],
            list1[2],
        )
    )
    print(data)


url = "https://www.racefans.net/"
content = requests.get(url)
page = BeautifulSoup(content.text, "lxml")
class_total = re.compile("post-.*")
totalArticles = page.findAll("article", {"id": class_total})

for i in range(0, 15):
    basic_data(totalArticles[i])
save()

import numpy as np
import pandas as pd
import requests
from bs4 import  BeautifulSoup


def url_script(url):
    page=requests.get(url)
    soup=BeautifulSoup(page.text,'lxml')
    text=[p.text for p in soup.find(
        class_='elementor-element elementor-element-74af9a5b elementor-widget elementor-widget-theme-post-content'
    )]
    print(url)
    return text

url=url_script("https://scrapsfromtheloft.com/books/umberto-eco-narrative-structure-ian-fleming/")
print(url)

df=pd.DataFrame()
df['raw-data']=np.array(url)
df.head()
df.to_excel("articles.xlsx",index=True)

# df_2=pd.read_csv("articles.xlsx")
# df_2.head()
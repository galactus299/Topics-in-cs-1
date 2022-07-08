from bs4 import BeautifulSoup
import requests
import pandas as pd

url="https://www.nytimes.com/interactive/2017/06/23/opinion/trumps-lies.html?mtrref=undefined&assetType=PAYWALL&mtrref=www.nytimes.com&gwh=DE1FC0970889182BF755B94EC4A99B37&gwt=pay&assetType=PAYWALL"
list1=[]
data=requests.get(url)
res=BeautifulSoup(data.text,'lxml')
requests=res.find_all('span')


for items in requests:
    try:
        date=items.find('strong').text[0:-1]
        statement=items.contents[1][1:-2]
        truth=items.find('span').text
        link=items.find('a')['href']
        list1.append((date,statement,truth,link))

    except:
        continue
print(list1)
df=pd.DataFrame(list1,columns=["Date","Statement","Truth","link"])
df.to_csv("trumps_lies.csv")

import wikipedia
import pandas as pd
import random
df=pd.DataFrame(columns=['content','url','Title',"category",'summary',"link","reference"])

searchlist=wikipedia.search("Coronavirus", results=5)
x=0
for items in searchlist:
    list1=[]
    try:
        page=wikipedia.page(items)
    except wikipedia.DisambiguationError as e:
        s=random.choice(e.options)
        page=wikipedia.page(s,auto_suggest=False)



    df.loc[x,'url']=page.url
    df.loc[x, 'content'] = page.content
    df.loc[x, 'Title'] = page.title
    df.loc[x, 'summary'] = page.summary
    df.loc[x, 'link'] = page.links
    df.loc[x, 'reference'] = page.references
    x=x+1
    # df['url']=["".join(page.url)]
    # df['content']=["".join(page.content)]
    # df['Title']=["".join(page.title)]
    # df['summary']=["".join(page.summary)]
    # df['link']=["".join(page.links)]
    # df['reference']=["".join(page.references)]
print(df)

df.to_csv("wekipediatest.csv",index=False)




# for items in searchlist:
#     page=wikipedia.page(items)
#     print(page)
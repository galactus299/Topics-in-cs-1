import re
import numpy as np
import pandas as pd
import nltk

import string
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords





def pre_processing(data_text):
     documents = []
     stemmer = WordNetLemmatizer()
     for sen in range(0, len(data_text)):
          document = re.sub(r'\W', ' ', str(data_text[sen]))
          document = re.sub(re.escape(string.punctuation), '', document)
          document = re.sub(r'\s+[a-zA-Z]\s+', ' ', document)
          document = re.sub(r'\^[a-zA-Z]\s+', ' ', document)
          document = re.sub(r'\s+', ' ', document, flags=re.I)
          document = re.sub(r'^b\s+', '', document)
          document = re.sub(r'^\s', '', document)
          document = re.sub(r'\s$', '', document)
          document = document.lower()

          document = document.split()
          document = [stemmer.lemmatize(word) for word in document]
          document = ' '.join(document)
          document = [word for word in document.split() if word not in stopwords.words("english")]
          document = ' '.join(document)

          if (re.search(r'^\s*$', document) != None):
               continue
          if not document:
               continue

          documents.append(document)
     return documents

df=pd.read_csv('articles.csv')

documents=pre_processing(df['raw-data'])
# df['new']=documents
# df.to_csv('new.csv')
print(df)
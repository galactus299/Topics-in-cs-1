import pandas as pd
import re
from textblob import TextBlob
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import seaborn as sns
import nltk


data = pd.read_csv("blogs.csv")
# print(data.head())

# Step 1: Cleaning the text


def clean(text):
    # Removes all special characters and numericals leaving the alphabets
    text = re.sub("[^A-Za-z]+", " ", text)
    return text

def tokenize(test):
    text=nltk.word_tokenize(test)
    return text
# Step 2: Text blob sentiments analysis


def sentiment_analysis(mydata, col):
    def getSubjectivity(text):
        return TextBlob(text).sentiment.subjectivity

    # Create a function to get the polarity
    def getPolarity(text):
        return TextBlob(text).sentiment.polarity

    # step3 features extraction
    def features(text):
        score = SentimentIntensityAnalyzer().polarity_scores(text)
        return score["pos"], score["neg"], score["neu"], score["compound"]

    # Create two new columns ‘Subjectivity’ & ‘Polarity’
    newcol = col + "_Subjectivity"
    mydata[newcol] = mydata[col].apply(getSubjectivity)
    newcol1 = col + "_Polarity"
    mydata[newcol1] = mydata[col].apply(getPolarity)
    newcol3 = col + "_len"
    mydata[newcol3] = mydata[col].apply(lambda x: len(x.split()))
    mydata["positive"] = mydata[col].apply(features)
    mydata["positive"], mydata["negative"], mydata["neutral"], mydata["compound"] = zip(
        *mydata[col].map(features)
    )

    # feature engineering introduced a class label based on polarity score
    def getAnalysis(score):
        if score < 0:
            return "Negative"
        elif score == 0:
            return "Neutral"
        else:
            return "Positive"

    newcol2 = col + "_Analysis"
    mydata[newcol2] = mydata[newcol1].apply(getAnalysis)
    return mydata


# plotting the dataset using matplot
def ploting(mydata):
    mydata.plot(kind="bar", x="Cleaned_essay_len", y="Cleaned_essay_Subjectivity")
    plt.show()
    mydata.plot(kind="bar", x="Cleaned_essay_len", y="Cleaned_essay_Polarity")
    plt.show()
    mydata.plot(
        kind="scatter", x="Cleaned_essay_Subjectivity", y="Cleaned_essay_Polarity"
    )
    plt.show()
    mydata.plot(x="Cleaned_essay_Subjectivity", y="Cleaned_essay_Polarity")
    plt.show()
    mydata.plot(kind="box", x="Cleaned_essay_Subjectivity", y="Cleaned_essay_Polarity")
    plt.show()


# plotting with seaborn


def plottingsea(mydata):
    # sns.countplot(x="Cleaned_essay_Analysis", data=mydata)
    # plt.show()
    sns.scatterplot(
        x="Cleaned_essay_Subjectivity",
        y="Cleaned_essay_Subjectivity",
        data=mydata,
        hue="writers_names",
        palette="dark"

    )
    plt.title("scatter plot", fontsize= 10)
    plt.show()
    sns.histplot(x='writers_names', data=mydata, hue='writers_names', multiple='stack' )
    plt.title('Count of Writers ', fontsize=20)
    plt.xlabel('Writers Names', fontsize=16)
    plt.ylabel('Number of Essays', fontsize=16)
    plt.show()
    sns.pairplot(mydata)
    plt.show()
    corr = mydata.corr()
    sns.heatmap(corr)
    plt.show()


mydata = pd.DataFrame()
mydata["Cleaned_summary"] = data["article_summary"].apply(clean)

mydata["Cleaned_essay"] = data["article_essay"].apply(clean)
# mydata["Cleaned_essay"]=data["Cleaned_essay1"].apply(tokenize())
mydata["writers_names"] = data["article_autor_name"].apply(clean)
mydata = sentiment_analysis(mydata, "Cleaned_essay")
print(mydata.head(16))
mydata.to_csv("test.csv", index=True)
ploting(mydata)
plottingsea(mydata)
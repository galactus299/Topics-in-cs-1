import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import time
from sklearn.metrics import classification_report, confusion_matrix

df = pd.read_csv("test.csv")


X = df.drop(["Cleaned_essay_Analysis"], axis=1)
Y = df["Cleaned_essay_Analysis"]
X = pd.get_dummies(X)
Y = LabelEncoder().fit_transform(Y)
X = StandardScaler().fit_transform(X)


def forest_test(X, Y):
    X_Train, X_Test, Y_Train, Y_Test = train_test_split(
        X, Y, test_size=0.30, random_state=101
    )
    start = time.process_time()
    trainedforest = RandomForestClassifier(n_estimators=700).fit(X_Train, Y_Train)
    print(time.process_time() - start)
    predictionforest = trainedforest.predict(X_Test)
    print(confusion_matrix(Y_Test, predictionforest))
    print(classification_report(Y_Test, predictionforest))


forest_test(X, Y)

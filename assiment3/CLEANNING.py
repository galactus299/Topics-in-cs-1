import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("raceblogdata.csv")

# Empty Cells Remove
new_df = df.dropna()

# removing Dublicates
df.drop_duplicates(inplace=True)

# dateformat
df["article_update_date"] = pd.to_datetime(df["article_update_date"])
df["article_publish_date"] = pd.to_datetime(df["article_publish_date"])

df["ariticle_comments"].plot(kind = 'hist')

plt.show()

df['article_publish_date'].fillna((df['article_publish_date'].mean()), inplace=True)
print(new_df.to_string())
df.to_csv("new_formatted.csv",index=False)
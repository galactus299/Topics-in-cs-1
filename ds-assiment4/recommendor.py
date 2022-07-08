# Import Pandas
import pandas as pd

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1000)
pd.set_option("display.colheader_justify", "center")
pd.set_option("display.precision", 3)

# Load Movies Metadata
metadata = pd.read_csv("top50.csv", encoding="ISO-8859-1")

# Print the first three rows
print(metadata.head(3))

df_songs = metadata[
    ["Track.Name", "Beats.Per.Minute", "Energy", "Genre", "Popularity", "Artist.Name"]
]
print((df_songs.head(10)))

df_items = df_songs.pivot_table(
    index="Artist.Name", columns=["Track.Name"], values="Popularity"
).fillna(0)
print(df_items.head(5))


def get_recommendations(df, item):

    recommendations = df.corrwith(df[item])
    recommendations.dropna(inplace=True)
    recommendations = pd.DataFrame(
        recommendations, columns=["correlation"]
    ).reset_index()
    recommendations = recommendations.sort_values(by="correlation", ascending=False)

    return recommendations


# Create recomendations like this
recommendations = get_recommendations(df_items, "I Don't Care (with Justin Bieber)")
print(recommendations.head())

recommendations = get_recommendations(
    df_items, "Sunflower - Spider-Man: Into the Spider-Verse"
)
print(recommendations.head())

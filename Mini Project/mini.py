import numpy as np
import pandas as pd
import matplotlib.pylab as plt

players = {
    "player": ["Messi", "mbappe", "haaland", "Ronaldo", "Kane"],
    "Goals": [5, 7, 6, 4, 3],
    "Assists": [3, 2, 4, 1, 2]
}

df = pd.DataFrame(players)

print("====== FIFA Dashboard ======")

print("\nplayer Data:")
print(df)

print("\nTotal Goals", df["Goals"].sum())
print("\nAverage Goals", df["Goals"].mean())
print("\nHighest Goals", df["Goals"].max())
print("\nLowest Goals", df["Goals"].min())

top_scorer = df[df["Goals"] == df["Goals"].max()]
print("\nTop Scorer:")
print(top_scorer)

plt.bar(df["player"], df["Goals"])
plt.title("FIFA Player Goals")
plt.xlabel("Players")
plt.ylabel("Goals")
plt.show()
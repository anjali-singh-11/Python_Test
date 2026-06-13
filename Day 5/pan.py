import pandas as pd
fifa = {
    "players": ["Ronaldo", "Messi", "Mbappe", "Haaland"],
    "goals": [5, 7, 6, 8]
}

df = pd.DataFrame(fifa)

print("Total Goals", df["goals"].sum())
print("Average Goals", df["goals"].mean())
print("Highest Goals", df["goals"].max())
print("Lowest Goals", df["goals"].min())

print("\nTop Scorer:")
print(df[df["goals"] == df["goals"].max()])
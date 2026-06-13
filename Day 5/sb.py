import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

players = {
    "player": ["Messi", "mbappe", "haaland", "Ronaldo", "Kane"],
    "Goals": [5, 7, 6, 8, 3]
}

df = pd.DataFrame(players)
sns.barplot(x="player", y="Goals", data=df)
plt.show()

sns.lineplot(x="player", y="Goals", data=df)
plt.show()
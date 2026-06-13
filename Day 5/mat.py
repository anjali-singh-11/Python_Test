import matplotlib.pyplot as plt

players = ["Ronaldo", "Messi", "Mbappe", "Haaland"]

goals = [5, 7, 8, 6]

plt.bar(players, goals)
plt.title("fifa goals")
plt.xlabel("Players")
plt.ylabel("goals")
plt.show()

plt.plot(players, goals)
plt.show()
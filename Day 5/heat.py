import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

data = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

sns.heatmap(data, annot=True)

plt.title("Student Marks Heatmap")
plt.show()
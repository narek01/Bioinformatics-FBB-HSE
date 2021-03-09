import pandas as pd
from scipy.stats import randint
import seaborn as sns
import matplotlib.pyplot as plt

N = 2000000
counts = {}
values = []

for i in range(N):
    k = sum(randint.rvs(1, 7, size=2))
    counts[k] = counts.get(k, 0) + 1
    values.append(k)

df = pd.DataFrame({
    "k": [k for k in counts.keys()],
    "freq": [counts[k] / N for k in counts.keys()]
})

print(df)
sns.barplot(data=df, x="k", y="freq")
plt.tight_layout()
#plt.savefig("Task3_two_dices.png", dpi=900)
plt.show()

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sum = 0
for k in range(1, 1001):
    sum += 1 / (k ** 3)

df = pd.DataFrame(columns=["Value","Probability"])
for k in range(1, 11):
    df.loc[k, 'Value'] = k
    df.loc[k, 'Probability'] = (1 / (k ** 3)) / sum
df = df.apply(pd.to_numeric)

print('Normalization factor: ', sum, '\nProbability sum: ', df['Probability'].sum())

sns.relplot(data=df, x="Value", y="Probability", kind='line')
plt.tight_layout()
#plt.savefig("Task1_Power_law.png", dpi=900)
plt.show()

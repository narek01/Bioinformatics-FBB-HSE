import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("TCGA-COAD.tsv", sep='\t')
top1 = df[['Gene','TCGA-A6-2671-11A']].sort_values('TCGA-A6-2671-11A', ascending=False).iloc[0:100]
top2 = df[['Gene','TCGA-A6-2675-11A']].sort_values('TCGA-A6-2675-11A', ascending=False).iloc[0:100]
intersection = top1.join(top2, how='inner', rsuffix='_2').drop('Gene_2', axis=1)
print(intersection)

sns.scatterplot(data=intersection, x='TCGA-A6-2671-11A', y='TCGA-A6-2675-11A')
plt.tight_layout()
plt.show()
print(ds)

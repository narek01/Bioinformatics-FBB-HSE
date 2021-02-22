import pandas as pd

df = pd.read_csv("TCGA-COAD.tsv", sep='\t')

top1 = df[['Gene','TCGA-A6-2671-11A']].sort_values('TCGA-A6-2671-11A', ascending=False).iloc[0:100]
top2 = df[['Gene','TCGA-A6-2675-11A']].sort_values('TCGA-A6-2675-11A', ascending=False).iloc[0:100]
print(top1)
print(top2)

intersection = top1.join(top2, how='inner', rsuffix='_2').drop('Gene_2', axis=1)
print(intersection)

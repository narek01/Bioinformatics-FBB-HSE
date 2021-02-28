import pandas as pd
import numpy as np
from scipy.stats.mstats import gmean

df = pd.read_csv("TCGA-COAD_cancer_normal.tsv", sep="\t", index_col=0)
df = df.loc[df.min(axis=1) > 0]
df = df.assign(Pseudo=np.zeros(df.shape[0]))
df.Pseudo = gmean(df.iloc[:,:-1], axis=1)
df = df.div(df.Pseudo, axis=0)
print(df.median(axis=0)[:-1])

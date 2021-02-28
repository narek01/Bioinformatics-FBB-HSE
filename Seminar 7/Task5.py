import pandas as pd
import numpy as np

df = pd.read_csv("TCGA-COAD_cancer_normal.tsv", sep="\t", index_col=0)
gl = pd.read_csv("gene_lengths.tsv", sep="\t", index_col=0).sort_index()

RPM = df.div(df.sum(axis=0) / 10**6, axis=1)
RPKM = RPM.div(gl["Length"] / 10**3, axis=0)

size_factors = [0.35219656, 0.39439086, 0.73057344, 1.66138079, 1.60002838, 1.48313616, 1.28046971, 0.92434274, 1.59306799, 1.34997698]
RPKM = RPKM.div(size_factors, axis=1)
df = np.log2(RPKM + 1)
df = df.loc[df.max(axis=1) > 0]
df["median"] = df.median(axis=1)
df = df.sort_values("median", ascending=False)
df = df.iloc[:len(df)//2]

df["Diff"] = df.max(axis=1) / df.min(axis=1)
df = df.sort_values("Diff", ascending=True)

print(df.head(10))

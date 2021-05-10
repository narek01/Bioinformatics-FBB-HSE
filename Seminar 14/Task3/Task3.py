import numpy as np, pandas as pd
from scipy.stats import spearmanr, pearsonr

"""
# Готовим табличку

df = pd.read_csv("healthy_breast.tsv", sep="\t", index_col=0)
sp = list()
pv = list()
for gene in df.index:
    corr = spearmanr(df.loc["SPI1"][:110], df.loc[gene][:110])
    sp.append(round(corr[0], 4))
    pv.append(round(corr[1], 4))
df["Spearman"] = sp
df["pvalue"] = pv
df.to_csv("healthy_breast_SPI1_spearman.tsv", sep="\t", columns=["Spearman", "pvalue"])
"""
df = pd.read_csv("https://raw.githubusercontent.com/narek01/Bioinformatics-FBB-HSE/main/Seminar%2014/Task3/healthy_breast_SPI1_spearman.tsv", sep="\t", index_col=0)

df = df.sort_values(by="Spearman", ascending = False, key=np.abs).loc[np.abs(df["Spearman"]) >= 0.8]

#df.to_csv("healthy_breast_SPI1_spearman08.tsv", sep="\t")

# Проверили, все ли pvalue значимые. Ответ: да
#print(np.unique(df["pvalue"]))

print("\n".join(df.index))

"""
Судя по куче белков CD и некоторым другим генам, SPI1 регулирует гены, отвечающие за иммунный ответ.

"""

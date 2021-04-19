import numpy as np
import pandas as pd
from scipy.stats import ttest_rel, ttest_ind

df = pd.read_csv('https://raw.githubusercontent.com/s-a-nersisyan/HSE_bioinformatics_2021/master/seminar12/colon_cancer_tumor_vs_normal_paired_FPKM.tsv', sep = '\t', index_col = 0)

df['p-value-ind'] = [ttest_ind(df.loc[gene].iloc[0:5], df.loc[gene].iloc[5:10])[1] for gene in df.index]
unpair = df['p-value-ind'][df['p-value-ind'] < 0.05].sort_values()
print("Unpair test:", unpair.size, "genes.")

df['p-value-rel'] = [ttest_rel(df.loc[gene].iloc[0:5], df.loc[gene].iloc[5:10])[1] for gene in df.index]
pair = df['p-value-rel'][df['p-value-rel'] < 0.05].sort_values()
print("Pair test:", pair.size, "genes.")

#print(pair.head(10))
#print(unpair.head(10))

print('\nCommon genes:', *(set(pair.head(10).index) & set(unpair.head(10).index)))

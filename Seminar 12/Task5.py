import numpy as np
import pandas as pd
from scipy.stats import shapiro

df = pd.read_csv('https://raw.githubusercontent.com/s-a-nersisyan/HSE_bioinformatics_2021/master/seminar11/breast_cancer_1000_genes.tsv', sep = '\t', index_col = 0)

df['test'] = [shapiro(df.loc[gene]).pvalue for gene in df.index]
df_normal = df[df['test'] > 0.05] # Не отклоняем нулевую гипотезу

print(round(df_normal.size/df.size*100, 2), "%")

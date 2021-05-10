import numpy as np, pandas as pd
from scipy.stats import spearmanr, pearsonr
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("BRCA_pam50.tsv", sep="\t", index_col=0)
genes = ["ESR1", "PGR", "ERBB2", "MKI67"]

def boxplot(gene):
    plt.figure(figsize=(8, 5))
    ax = sns.boxplot(data=df, y=gene, x="Subtype")
    ax.set_ylabel("Expression")
    ax.set_title(gene)
    plt.tight_layout()
    plt.savefig(gene, dpi=350)
    plt.close()

[boxplot(gene) for gene in genes]

"""
Normal-like: уровень экспрессии всех генов средний относительно других подтипов.
Luminal A: сильно экспрессирует ESR1.
Luminal B: как Luminal A, но экспрессия MKI67 выше.
Triple-negative: ESR1 и PGR экспрессированы очень слабо, а MKI67 очень сильно.
HER2-enriched: ESR1 слабо, а PGR очень слабо экспрессированы, а MKI67 очень сильно.
Healthy: как Normal-like, но экспрессия MKI67 ниже.

"""

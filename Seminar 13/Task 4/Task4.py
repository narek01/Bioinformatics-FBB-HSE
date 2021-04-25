import pandas as pd
from scipy.stats import ttest_ind, mannwhitneyu
import seaborn as sns
import matplotlib.pyplot as plt

def violin(df, name):
    sns.violinplot(data=df).set_title(name)
    plt.savefig(name, dpi=300)
    plt.close()

unpaired_FPKM_path = "https://raw.githubusercontent.com/s-a-nersisyan/HSE_bioinformatics_2021/master/seminar13/colon_cancer_tumor_vs_normal_unpaired_FPKM.tsv"
deseq = pd.read_csv("https://raw.githubusercontent.com/narek01/Bioinformatics-FBB-HSE/main/Seminar%2013/Task 2/DESeq2_results_paired.tsv", sep="\t", index_col=0)["padj"][:10]

df = pd.read_csv(unpaired_FPKM_path, sep="\t", index_col=0)

ttest = pd.DataFrame([ttest_ind(df.loc[gene].iloc[0:5], df.loc[gene].iloc[5:10])[1] for gene in df.index], index=df.index, columns=["t-test"])
ttest = ttest.sort_values("t-test")[:10]

mw = pd.DataFrame([mannwhitneyu(df.loc[gene].iloc[0:5], df.loc[gene].iloc[5:10])[1] for gene in df.index], index=df.index, columns=["mannwhitney"])
mw = mw.sort_values("mannwhitney")[:10]

violin(deseq, "DESeq2")
violin(ttest, "T-test")
violin(mw, "Mann-Whitney")

import pandas as pd
from scipy.stats import ttest_ind, mannwhitneyu

paired_FPKM_path = "https://raw.githubusercontent.com/s-a-nersisyan/HSE_bioinformatics_2021/master/seminar13/colon_cancer_tumor_vs_normal_paired_FPKM.tsv"
unpaired_FPKM_path = "https://raw.githubusercontent.com/s-a-nersisyan/HSE_bioinformatics_2021/master/seminar13/colon_cancer_tumor_vs_normal_unpaired_FPKM.tsv"
paired_counts_path = "https://raw.githubusercontent.com/s-a-nersisyan/HSE_bioinformatics_2021/master/seminar13/colon_cancer_tumor_vs_normal_paired_counts.tsv"
unpaired_counts_path = "https://raw.githubusercontent.com/s-a-nersisyan/HSE_bioinformatics_2021/master/seminar13/colon_cancer_tumor_vs_normal_unpaired_counts.tsv"

"""
from rpy2 import robjects
from rpy2.robjects import Formula

from rpy2.robjects import pandas2ri
pandas2ri.activate()

from rpy2.robjects.packages import importr

base = importr("base")
stats = importr("stats")
DESeq2 = importr("DESeq2")


def deseq(meta, formula):
    meta["Tissue"] = stats.relevel(robjects.vectors.FactorVector(meta["Tissue"]), ref="Normal")
    # Calculate normalization factors
    dds = DESeq2.DESeqDataSetFromMatrix(countData=counts, colData=meta, design=Formula(formula))
    dds = DESeq2.DESeq(dds)
    res = DESeq2.results(dds, name="Tissue_Tumor_vs_Normal")
    res = DESeq2.lfcShrink(dds, coef="Tissue_Tumor_vs_Normal", type="apeglm")
    res = pd.DataFrame(base.as_data_frame(res))
    res.index = counts.index
    res = res.sort_values("padj")
    res = res.loc[res["padj"] < 0.05]
    res = res.loc[res["log2FoldChange"].abs() >= 1]
    return res

# DESeq2
counts = pd.read_csv(unpaired_counts_path, sep="\t", index_col=0)
meta_unpaired = pd.DataFrame({"Tissue": ["Tumor"]*5 + ["Normal"]*5}, index=counts.columns)
unpaired_res = deseq(meta_unpaired, "~ Tissue")
unpaired_res.to_csv("DESeq2_results_unpaired.tsv", sep="\t")

"""

def intersections(df1, df2, methods):
    common = ", ".join(set(df1.index[:10]) & set(df2.index[:10]))
    if common:
        print(f"\n{methods} common genes:", common)
    else:
        print(f"\nNo common genes between {methods} methods")


deseq = pd.read_csv("https://raw.githubusercontent.com/narek01/Bioinformatics-FBB-HSE/main/Seminar%2013/Task%203/DESeq2_results_unpaired.tsv", sep="\t", index_col=0)["padj"][:10]

df = pd.read_csv(unpaired_FPKM_path, sep="\t", index_col=0)

ttest = pd.DataFrame([ttest_ind(df.loc[gene].iloc[0:5], df.loc[gene].iloc[5:10])[1] for gene in df.index], index=df.index, columns=["t-test"])
ttest = ttest.sort_values("t-test")[:10]

mw = pd.DataFrame([mannwhitneyu(df.loc[gene].iloc[0:5], df.loc[gene].iloc[5:10])[1] for gene in df.index], index=df.index, columns=["mannwhitney"])
mw = mw.sort_values("mannwhitney")[:10]

intersections(deseq, mw, "DESeq2 and Mann-Whitney")
intersections(deseq, ttest, "DESeq2 and t-test")
intersections(mw, ttest, "Mann-Whitney and t-test")

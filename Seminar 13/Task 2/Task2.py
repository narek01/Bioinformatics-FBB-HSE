import pandas as pd

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


# Load read counts table
paired_FPKM_path = "https://raw.githubusercontent.com/s-a-nersisyan/HSE_bioinformatics_2021/master/seminar13/colon_cancer_tumor_vs_normal_paired_FPKM.tsv"
unpaired_FPKM_path = "https://raw.githubusercontent.com/s-a-nersisyan/HSE_bioinformatics_2021/master/seminar13/colon_cancer_tumor_vs_normal_unpaired_FPKM.tsv"
paired_counts_path = "https://raw.githubusercontent.com/s-a-nersisyan/HSE_bioinformatics_2021/master/seminar13/colon_cancer_tumor_vs_normal_paired_counts.tsv"
unpaired_counts_path = "https://raw.githubusercontent.com/s-a-nersisyan/HSE_bioinformatics_2021/master/seminar13/colon_cancer_tumor_vs_normal_unpaired_counts.tsv"

counts = pd.read_csv(paired_counts_path, sep="\t", index_col=0)

# Define meta
meta_paired = pd.DataFrame({"Tissue": ["Tumor"]*5 + ["Normal"]*5, "Pairs": ["1","2","3","4","5"]*2}, index=counts.columns)
meta_unpaired = pd.DataFrame({"Tissue": ["Tumor"]*5 + ["Normal"]*5}, index=counts.columns)

paired_res = deseq(meta_paired, "~ Tissue + Pairs")
unpaired_res = deseq(meta_unpaired, "~ Tissue")
"""

paired_res = pd.read_csv("https://raw.githubusercontent.com/narek01/Bioinformatics-FBB-HSE/main/Seminar%2013/Task 2/DESeq2_results_paired.tsv", sep="\t", index_col=0)
unpaired_res = pd.read_csv("https://raw.githubusercontent.com/narek01/Bioinformatics-FBB-HSE/main/Seminar%2013/Task2/DESeq2_results_unpaired.tsv", sep="\t", index_col=0)

print("Paired:", len(paired_res.loc[paired_res["padj"] < 0.05]), "genes are differential expressed. Top-10:", ", ".join(set(paired_res.index[:10])))
# Paired: 3847 genes are differential expressed. Top-10: GYLTL1B, KRT80, MMP7, CST1, TRIM29, GRIN2D, KLK10, C2CD4A, CDH3, RP11-474D1.3
print("\nUnpaired:", len(unpaired_res.loc[unpaired_res["padj"] < 0.05]), "genes are differential expressed. Top-10:", ", ".join(set(unpaired_res.index[:10])))
# Unpaired: 3698 genes are differential expressed. Top-10: GYLTL1B, SPTBN2, WNT2, MMP11, CEMIP, C2CD4A, TRIB3, CDH3, RP11-474D1.3, ATG9B
print("\nCommon genes:", ", ".join(set(paired_res.index[:10]) & set(unpaired_res.index[:10])))
# Common genes: GYLTL1B, RP11-474D1.3, C2CD4A, CDH3

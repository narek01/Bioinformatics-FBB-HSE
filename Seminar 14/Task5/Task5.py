import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE

df = pd.read_csv("human_coronavirus_aln_scores.tsv", sep="\t", index_col=0)
df = 5000/df
perplexities = [5, 30, 50, 100]

def tsne_func(perpl):
    Y = TSNE(n_components=2, perplexity=perpl, metric = "precomputed").fit_transform(df)
    Y = pd.DataFrame(Y, columns=["PC1", "PC2"])
    viruses = []
    for virus in ["HCoV-HKU1", "MERS-CoV", "SARS-CoV-2", "HCoV-229E", "HCoV-NL63", "HCoV-OC43", "SARS-CoV"]:
        [viruses.append(virus) for i in range(20)]
    Y["Virus"] = viruses
    print(Y)
    ax = sns.scatterplot(x="PC1", y="PC2", data=Y, hue="Virus")
    ax.set_title(f"Perplexity = {perpl}")
    plt.legend(frameon=False)
    plt.tight_layout()
    #plt.show()
    plt.savefig(f"Perplexity_{perpl}", dpi=350)
    plt.close()

[tsne_func(p) for p in perplexities]

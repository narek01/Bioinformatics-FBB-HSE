import pandas as pd

all_genes = pd.read_csv("https://raw.githubusercontent.com/s-a-nersisyan/HSE_bioinformatics_2021/master/seminar13/all_genes.txt", header=None)[0]

df = pd.DataFrame(index=all_genes)
for i in range(1, 6):
    df.sample(1000).to_csv(f"./Sample{i}.txt", header = False)

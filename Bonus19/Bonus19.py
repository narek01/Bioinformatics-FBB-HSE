#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import make_scorer
from sklearn.metrics import accuracy_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import GridSearchCV


# In[2]:


def res(cv):
    par, s = cv.best_params_, cv.best_score_
    print("Number of neighbors:", par['clf__n_neighbors'])
    print("Weights:", par['clf__weights'])
    if par['clf__p'] == 1:
        p = "Manhattan"
    elif par['clf__p'] == 2:
        p = "Euclidean"
    print(p, "metric is used")
    print("Best score is:", str(round(100*s, 1)) + "%")


# In[3]:


df = pd.read_csv("BRCA_pam50.tsv", sep="\t", index_col=0)
X = df.iloc[:, :-1].to_numpy()
y = df["Subtype"].to_numpy()


# In[4]:


X_tsne = TSNE(n_components=2, perplexity=30).fit_transform(X)
X_pca = PCA(n_components=2).fit_transform(X)


# In[5]:


model = Pipeline([
    ("scaler", StandardScaler()),
    ("clf", KNeighborsClassifier(n_jobs=-1))
])


# In[6]:


params = {
    "clf__n_neighbors": [1, 2, 3, 4, 5, 6, 7, 8, 9],
    "clf__weights": ["uniform", "distance"],
    "clf__p": [1, 2]
}

cv = GridSearchCV(
    model, params, n_jobs=-1,
    scoring=make_scorer(accuracy_score),
    cv=RepeatedStratifiedKFold(n_repeats=20)
)


# In[7]:


# 50 dimensions
cv.fit(X, y)
res(cv)


# In[8]:


# t-SNE: 2 dimensions
cv.fit(X_tsne, y)
res(cv)


# In[9]:


# PCA: 2 dimensions
cv.fit(X_pca, y)
res(cv)


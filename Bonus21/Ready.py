#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from catboost import CatBoostClassifier, Pool
from sklearn.metrics import balanced_accuracy_score, confusion_matrix
import pickle
from catboost.utils import get_gpu_device_count


# In[2]:


def accuracy(X_test, y_test, model):
    y_pred = model.predict(X_test)
    M = confusion_matrix(y_test, y_pred)
    print(M)
    TPR = M[0, 0] / (M[0, 0] + M[0, 1])
    TNR = M[1, 1] / (M[1, 0] + M[1, 1])
    print(round(TPR, 2), round(TNR, 2), '\n')


genes = ['HOXA7', 'FABP6', 'GRIP2', 'VEGFA', 'AKAP12', 'RHEB', 'PMEPA1']

df = pd.read_pickle("cc_data.pkl").loc[:, ["FAP", "INHBA", "BGN", "MKI67", "MYC", "MYBL2", "GADD45B"]]
df = pd.read_pickle("cc_data.pkl").loc[:, ["FABP6", "AKAP12", "SLC9A3R1", "VEGFA", "MYC", ]]
ann = pd.read_pickle("cc_ann.pkl")

X = df.loc[ann.index].to_numpy()
y = ann["Class"].to_numpy()

X_train = df.loc[ann.loc[ann["Dataset type"] == "Training"].index].to_numpy()
y_train = ann.loc[ann["Dataset type"] == "Training", "Class"].to_numpy()

X_test1 = df.loc[ann.loc[ann["Dataset"] == "GSE14333"].index].to_numpy()
y_test1 = ann.loc[ann["Dataset"] == "GSE14333", "Class"].to_numpy()
X_test2 = df.loc[ann.loc[ann["Dataset"] == "GSE37892"].index].to_numpy()
y_test2 = ann.loc[ann["Dataset"] == "GSE37892", "Class"].to_numpy()
X_test3 = df.loc[ann.loc[ann["Dataset"] == "GSE33113"].index].to_numpy()
y_test3 = ann.loc[ann["Dataset"] == "GSE33113", "Class"].to_numpy()



model = CatBoostClassifier(random_seed=17,
                           od_type = "Iter",
                           num_trees=2000,
                           od_wait = 20,
                           learning_rate=0.05,
                           depth=4,
                           min_data_in_leaf=4,
                           subsample=0.88,
                           l2_leaf_reg=3,
                           verbose=True)
'''                   
grid = {'learning_rate': [0.001, 0.1],
        'depth': [4, 10],
        'l2_leaf_reg': [1, 3, 5, 7, 9],
        'bagging_temperature': [0, 1, 2]}
     
grid = {'learning_rate': [0.001, 0.1]}

grid_search_result = model.grid_search(grid,
                                       X=X_train,
                                       y=y_train,
                                       train_size=0.8)


         
randomized_search_result = model.randomized_search(grid,
                                                   X=X_train,
                                                   y=y_train,
                                                   n_iter=30)
'''                                        
model.fit(X_train, y_train)
print(model.get_all_params())

m = model
accuracy(X_test1, y_test1, m)
accuracy(X_test2, y_test2, m)
accuracy(X_test3, y_test3, m)
accuracy(X_train, y_train, m)


model.save_model("upgrading.cbm")
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


# In[3]:


df = pd.read_pickle("cc_data.pkl")
ann = pd.read_pickle("cc_ann.pkl")


# In[4]:


X_train = df.loc[ann.loc[ann["Dataset type"] == "Training"].index].to_numpy()
y_train = ann.loc[ann["Dataset type"] == "Training", "Class"].to_numpy()

X_test1 = df.loc[ann.loc[ann["Dataset"] == "GSE14333"].index].to_numpy()
y_test1 = ann.loc[ann["Dataset"] == "GSE14333", "Class"].to_numpy()
X_test2 = df.loc[ann.loc[ann["Dataset"] == "GSE37892"].index].to_numpy()
y_test2 = ann.loc[ann["Dataset"] == "GSE37892", "Class"].to_numpy()
X_test3 = df.loc[ann.loc[ann["Dataset"] == "GSE33113"].index].to_numpy()
y_test3 = ann.loc[ann["Dataset"] == "GSE33113", "Class"].to_numpy()


# In[ ]:





# In[ ]:


# initialize data
train_data = X_train
train_labels = y_train

model2 = CatBoostClassifier(task_type="GPU")
model2.fit(train_data, train_labels, verbose=True)


# In[ ]:


m = model2
accuracy(X_test1, y_test1, m)
accuracy(X_test2, y_test2, m)
accuracy(X_test3, y_test3, m)
accuracy(X_train, y_train, m)


model2.save_model("model2.cbm")

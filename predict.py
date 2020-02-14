#!/usr/bin/env python
# coding: utf-8

# ### On récupère les données

# In[36]:


import pandas as pd
import os

predict = pd.read_csv("predict.csv")


# In[37]:


from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

le = preprocessing.LabelEncoder()
predict = predict.astype(str)
predict = predict.apply(le.fit_transform)

scaler = StandardScaler()
X = scaler.fit_transform(predict)

pca = PCA(n_components= 73)
X = pca.fit_transform(X)


# In[38]:


from sklearn.externals import joblib
forest = joblib.load("finalized_model.sav")


# In[39]:


predict['Response'] = forest.predict(X)
predict.to_csv (r'result.csv', index = None, header=True)


# In[ ]:





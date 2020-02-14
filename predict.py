#!/usr/bin/env python
# coding: utf-8

# ### On récupère les données
import pandas as pd
import os

predict = pd.read_csv("predict.csv")



#pretraitement
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

#on encode les chaines de caracteres
le = preprocessing.LabelEncoder()
predict = predict.fillna(0)
predict.Product_Info_2 = le.fit_transform(predict.Product_Info_2.astype(str))
predict.InsuredInfo_7 = le.fit_transform(predict.InsuredInfo_7.astype(str))
predict.InsuredInfo_8 = le.fit_transform(predict.InsuredInfo_8.astype(str))
predict.InsuredInfo_9 = le.fit_transform(predict.InsuredInfo_9.astype(str))

#on normalise les dimensions
scaler = StandardScaler()
X = scaler.fit_transform(predict)

#on réduit le nnombre de dimensions
pca = PCA(n_components= 8)
X = pca.fit_transform(X)


#on recupere le modele entraine
from sklearn.externals import joblib
forest = joblib.load("finalized_model.sav")

#on cree le fichier CSV
predict['Response'] = forest.predict(X).round().astype(int)
predict.to_csv (r'result.csv', index = None, header=True)






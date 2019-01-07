# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import preprocessing 


dataset =pd.read_csv('chat_ansh.tsv', delimiter='\t',header=None)
y=dataset.iloc[:,2].values
x=dataset.iloc[:,3].values


   
le=preprocessing.LabelEncoder()
y=le.fit_transform(y)

from sklearn.feature_extraction.text import CountVectorizer
cv=CountVectorizer()
cv.fit(x)
X=cv.transform(x).toarray()

#naive-baise
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

from sklearn.naive_bayes import GaussianNB
clas=GaussianNB()
clas.fit(x_train,y_train)

y_pred=clas.predict(x_test)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

#input from console
print("----------------------")
while True:
    y_txt=[]
    y_txt.append(input())
    y_txt_pd=cv.transform(y_txt).toarray()
    y_res=clas.predict(y_txt_pd)
    
    y_res=(y_res>0.5)
    name=le.inverse_transform(y_res)
    print(name[0])
    
    
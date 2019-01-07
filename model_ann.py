# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 23:26:13 2018

@author: sumit
"""

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
X=cv.fit_transform(x).toarray()

#naive-baise
from sklearn.cross_validation import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

#nural net
import keras
from keras.models import Sequential
from keras.layers import Dense
 
clas=Sequential()
clas.add(Dense(output_dim=983,init='uniform' ,activation='relu',input_dim=int(x_test.size/y_test.size)))
clas.add(Dense(output_dim=283,init='uniform',activation='relu'))
clas.add(Dense(output_dim=483,init='uniform',activation='relu'))
clas.add(Dense(output_dim=1,init='uniform',activation='sigmoid'))

clas.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

clas.fit(x_train,y_train,batch_size=10,nb_epoch=2)
y_pred=clas.predict(x_test)

#probality to 0-1
y_pred=(y_pred>0.5)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)

#--------------- for input

print("----------------------")
while True:
    y_txt=[]
    y_txt.append(input())
    y_txt_pd=cv.transform(y_txt).toarray()
    y_res=clas.predict(y_txt_pd)
    
    y_res=int(y_res>0.5)
    
    name=le.inverse_transform(y_res)
    print(name)

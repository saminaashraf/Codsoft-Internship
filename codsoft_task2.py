# -*- coding: utf-8 -*-
"""CodSoft Task2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1v3k5q9HzEkPEGby0CyI2r3tdOKgcAX6j
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

file=pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Movies.csv', encoding='ISO-8859-1')

file
file1=file.fillna(0)
file1

X = file1[['Name', 'Year', 'Duration', 'Genre', 'Votes', 'Director', 'Actor 1', 'Actor 2','Actor 3']]
Y = file1['Rating']

X

Y

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

X_train

Y_train

model = LinearRegression()
model.fit(X_train, Y_train)



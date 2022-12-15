import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X = []
y = [1,1,1,1,1]
i = 0
file1 = open("src/Data/hatespeech.txt", 'r', encoding="utf8")
lines = file1.readlines()
for line in lines:
    for word in line:
        if word == "asian":
            X[i]+=1
    i+=1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

model_fit = LinearRegression()
model_fit.fit(X_train, y_train)
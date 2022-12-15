import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X = []
y = []
i = 0
file1 = open("src/Data/hatespeech.txt", 'r', encoding="utf8")
lines = file1.readlines()
file2 = open("src/Data/ids.txt", 'r', encoding="utf8")
id_lines = file2.readlines()
for i, h_line in enumerate(lines):
    if h_line == 'no data\n':
        continue
    X.append(0)
    res = h_line.split()
    for word in res:
        print(word)
        if word == "Asian":
            X[i]+=1
    #i+=1
    if id_lines[i].__contains__("racism"):
        y.append(0.8)
    elif id_lines[i].__contains__("sexism"):
        y.append(0.7)
    else:
        y.append(0)
print(X)
print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

model_fit = LinearRegression()
model_fit.fit(X_train, y_train)
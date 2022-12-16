import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import f1_score, precision_score, recall_score

X = []
y = []
file1 = open("src/Data/hatespeech.txt", 'r', encoding="utf8")
lines = file1.readlines()
file2 = open("src/Data/ids.txt", 'r', encoding="utf8")
id_lines = file2.readlines()
for i, h_line in enumerate(lines):
    X.append(0)
    if h_line == 'no data\n':
        y.append(0)
        continue
    res = h_line.split()
    for word in res:
        if word == "Asian" or word == "serbia" or word == "Serbian" or word == "Drasko":
            X[i]+=1
        elif word == "bitches" or word == "pimping" or word == "trashy" or word == "girls":
            X[i]+=1
    if id_lines[i].__contains__("racism"):
        y.append(0.8)
    elif id_lines[i].__contains__("sexism"):
        y.append(0.6)
    else:
        y.append(0)
#print(X)
#print(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

X_train = np.array(X_train).reshape(-1, 1)
X_test = np.array(X_test).reshape(-1, 1)
y_train = np.array(y_train).reshape(-1, 1)
y_test = np.array(y_test).reshape(-1, 1)

model_fit = LinearRegression().fit(X_train, y_train)

print('R2 Training Score: %.3f' % model_fit.score(X_train, y_train))
print('R2 Testing Score: %.3f' % model_fit.score(X_test, y_test))

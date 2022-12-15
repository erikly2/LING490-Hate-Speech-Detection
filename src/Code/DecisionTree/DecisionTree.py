#Ariane

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score
from sklearn.model_selection import KFold

# X = tweets
# Y = classification label

X = []
y = []
file1 = open("src/Data/hatespeech.txt", 'r')
lines = file1.readlines()
for i, line in enumerate(lines):
    for word in line:
        if word == "racism" or word == "sexism" or word == "none":
            Y[i] = word
        else:
            X[i] = line
            break

#train and evaluate based on the data to get the F1 Measure assements of the model prediction
def train_eval(classifier):
    kf = KFold(n_splits = 5)        # fold the data
    foldCounter = 0
    aList, bList, cList = list(), list(), list()
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        y_train, y_test = Y[train_index], Y[test_index]
        classifier.fit(X_train, y_train)
        y_pred = classifier.predict(X_test)
        f1 = f1_score(y_test, y_pred, average="micro")
        aList.append(f1)
        foldCounter += 1
    F1 = np.mean(aList)
    Precision = np.mean(bList)
    Recall = np.mean(cList)
    return F1, Precision, Recall

classifier = DecisionTreeClassifier()
print(train_eval(classifier))

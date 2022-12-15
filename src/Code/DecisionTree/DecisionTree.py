#Ariane

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score

from sklearn.model_selection import KFold
from sklearn import preprocessing

# X = tweets
# Y = classification label

X = []
Y = []
hatespeech_file = open("src/Data/hatespeech.txt", 'r')
id_file = open("src/Data/ids.txt", 'r')
hatespeech_lines = hatespeech_file.readlines()
id_lines = id_file.readlines()
#go through each line in hatespeech.txt and check if corresponding line in ids.txt contains hatespeech label
for i, h_line in enumerate(hatespeech_lines):
    X.append(h_line)
    if id_lines[i].__contains__("racism"):
        Y.append("racism")
    elif id_lines[i].__contains__("sexism"):
        Y.append("sexism")
    else:
        Y.append("none")

X = np.array(X)
Y = np.array(Y)


#train and evaluate based on the data to get the F1 Measure assements of the model prediction
def train_eval(classifier):
    kf = KFold(n_splits = 5)        # fold the data
    foldCounter = 0
    aList, bList, cList = list(), list(), list()
    for train_index, test_index in kf.split(X):
        X_train, X_test = X[train_index], X[test_index]
        Y_train, Y_test = Y[train_index], Y[test_index]
        #proc_classifier = preprocessing.LabelEncoder()
        train_x = pd.get_dummies(X_train)
        classifier.fit(train_x, Y_train)
        Y_pred = classifier.predict(train_x)

        f1 = f1_score(Y_test, Y_pred, average="micro")
        precision = precision_score(Y_test, Y_pred, average="micro")
        recall = recall_score(Y_test, Y_pred, average="micro")
        aList.append(f1)
        bList.append(precision)
        cList.append(recall)
        foldCounter += 1
    F1 = np.mean(aList)
    Precision = np.mean(bList)
    Recall = np.mean(cList)
    return F1, Precision, Recall

classifier = DecisionTreeClassifier()
print(train_eval(classifier))


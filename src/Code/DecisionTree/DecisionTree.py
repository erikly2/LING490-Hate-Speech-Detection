#Ariane

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import precision_score
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split



from sklearn.model_selection import KFold
from sklearn import preprocessing

# X = tweets
# Y = classification label

X = []
Y = []
hatespeech_file = open("src/Data/hatespeech.txt", 'r', encoding="utf8")
id_file = open("src/Data/ids.txt", 'r', encoding="utf8")
hatespeech_lines = hatespeech_file.readlines()
id_lines = id_file.readlines()
#go through each line in hatespeech.txt and check if corresponding line in ids.txt contains hatespeech label
for i, h_line in enumerate(hatespeech_lines):
    if h_line == 'no data\n':
        continue
    X.append(h_line)
    if id_lines[i].__contains__("racism"):
        Y.append("racism")
    elif id_lines[i].__contains__("sexism"):
        Y.append("sexism")
    else:
        Y.append("none")

X = np.array(X)
Y = np.array(Y)

X = pd.get_dummies(X).values
#test_x = pd.get_dummies(X).values
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)
print(len(X_train))
print(len(Y_train))
print(len(X_test))
print(len(Y_test))


classifier = DecisionTreeClassifier(random_state=0).fit(X_train, Y_train)

#model_fit = classifier.fit(X_train, Y_train)
print(classifier.score(X_train, Y_train))
print(classifier.score(X_test, Y_test))
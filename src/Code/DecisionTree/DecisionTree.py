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

#train and evaluate based on the data to get the F1 Measure assements of the model prediction

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

classifier = DecisionTreeClassifier()
print(classifier.fit(X_train, Y_train))

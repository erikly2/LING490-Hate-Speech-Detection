import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

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

#make string values into floats
X = pd.get_dummies(X).values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

classifier = GaussianNB()

model_fit = classifier.fit(X_train, Y_train)
Y_pred = classifier.predict(X_test)


print('R2 Training Score: %.3f' % model_fit.score(X_train, Y_train))
print('R2 Testing Score: %.3f' % model_fit.score(X_test, Y_test))	
print(classification_report(Y_test, Y_pred))
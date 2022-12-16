# # from sklearn.model_selection import train_test_split
# # from sklearn.naive_bayes import GaussianNB
# # from sklearn import preprocessing
# # from sklearn.metrics import f1_score
# # from sklearn.model_selection import KFold
# # import numpy as np
# # import matplotlib.pyplot as plt
# # import pandas as pd

# # def train_eval(classifier):
# #     kf = KFold(n_splits = 5)        
# #     foldCounter = 0
# #     aList, bList, cList = list(), list(), list()
# #     for train_index, test_index in kf.split(X):
# #         X_train, X_test = X[train_index], X[test_index]
# #         y_train, y_test = Y[train_index], Y[test_index]
# #         classifier.fit(X_train, y_train)
# #         y_pred = classifier.predict(X_test)
# #         f1 = f1_score(y_test, y_pred, average="micro")
# #         aList.append(f1)
# #         foldCounter += 1
# #     F1 = np.mean(aList)
# #     Precision = np.mean(bList)
# #     Recall = np.mean(cList)
# #     return F1, Precision, Recall

# # classifier = GaussianNB()
# # print(train_eval(classifier))
# from sklearn.naive_bayes import BernoulliNB
# from sklearn.svm import SVC
# from sklearn.model_selection import KFold
# from sklearn.metrics import f1_score, precision_score, recall_score
# import pandas as pd
import numpy as np
# from sklearn import preprocessing


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

# for i in range(len(all_data)):
#     X[i] += ['*'] * (max_length - len(X[i]))

# X = pd.DataFrame(X)

# def buildClassifiers(clf, X_train, X_test, y_train, y_test):

#     clf.fit(X_train, y_train)
#     y_pred = clf.predict(X_test)

#     f1 = f1_score(y_test, y_pred, average="micro", zero_division=0)
#     precision = precision_score(y_test, y_pred, average="micro", zero_division=0)
#     recall = recall_score(y_test, y_pred, average="micro", zero_division=0)

#     return f1, precision, recall

# names = ['Naive_Bayes']
# classifiers = [BernoulliNB()]

# for name, clf in zip(names, classifiers):

#     print('Now classifying', name)
#     kf = KFold(n_splits = 10, shuffle=True)
#     foldCounter = 0
#     aList, bList, cList = list(), list(), list()
#     for train_index, test_index in kf.split(X):
#         X_train, X_test = X.iloc[train_index], X.iloc[test_index]
#         y_train, y_test = np.take(Y, train_index), np.take(Y, test_index)

#         f1, precision, recall = buildClassifiers(clf, X_train, X_test, y_train, y_test)
#         aList.append(f1)
#         bList.append(precision)
#         cList.append(recall)

#         foldCounter += 1

#     print("\tAverage F1 for {}:\t\t".format(name), np.mean(aList))
#     print("\tAverage Precision for {}:\t".format(name), np.mean(bList))
#     print("\tAverage Recall for {}:\t\t".format(name), np.mean(cList))

import sklearn
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
train, test, train_labels, test_labels = train_test_split(
   X,Y,test_size = 0.40, random_state = 42
)
GNBclf = GaussianNB()
model = GNBclf.fit(train, train_labels)
preds = GNBclf.predict(test)
print(preds)
#Let’s build a simple naïve Bayes classification model and assess the accuracy.
#Essentially we can replace naïve Bayes with any other classification algorithm or use an
#ensemble model to build an efficient model

from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import Normalizer
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans, MiniBatchKMeans
import numpy as np

newsgroups_train = fetch_20newsgroups(subset='train')
print(list(newsgroups_train.target_names))

newsgroups_test = fetch_20newsgroups(subset='train')


categories = ['alt.atheism', 'comp.graphics', 'rec.motorcycles', 'sci.space', 'talk.politics.guns']

newsgroups_train = fetch_20newsgroups(subset='train', categories=categories,
                                      shuffle=True, random_state=2017, remove=('headers', 'footers', 'quotes'))
newsgroups_test = fetch_20newsgroups(subset='test', categories=categories,
                                     shuffle=True, random_state=2017, remove=('headers', 'footers', 'quotes'))

y_train = newsgroups_train.target
y_test = newsgroups_test.target

vectorizer = TfidfVectorizer(sublinear_tf=True, smooth_idf = True, max_df=0.5,  ngram_range=(1, 2), stop_words='english')
X_train = vectorizer.fit_transform(newsgroups_train.data)
X_test = vectorizer.transform(newsgroups_test.data)


from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

clf = MultinomialNB()
clf = clf.fit(X_train, y_train)

y_train_pred = clf.predict(X_train)
y_test_pred = clf.predict(X_test)

print ('Train accuracy_score: ', metrics.accuracy_score(y_train, y_train_pred))
print ('Test accuracy_score: ',metrics.accuracy_score(newsgroups_test.target, y_test_pred))

print ("Train Metrics: ", metrics.classification_report(y_train, y_train_pred))
print ("Test Metrics: ", metrics.classification_report(newsgroups_test.target, y_test_pred))
import nltk
import random
import pickle
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.classify import SklearnClassifier
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from statistics import mode

class VotedByClassifiers():
    def __init__(self,*classifiers):
        self.classifiers = classifiers
    
    def classify(self,features):
        votes = []
        for i in self.classifiers:
            v = i.classify(features)
            votes.append(v)

        return mode(votes)

    def accuracy_level(self,features):
        votes = []
        for i in self.classifiers:
            v = i.classify(features)
            votes.append(v)

        count_of_results = votes.count(mode(votes))
        accu = count_of_results/len(votes)
        return accu
    

read_pickle = open("pickles/documents.pickle","rb")
documents = pickle.load(read_pickle)
read_pickle.close()

read_pickle = open("pickles/word_features.pickle","rb")
word_features = pickle.load(read_pickle)
read_pickle.close()

def d_features(document):
    word = word_tokenize(document)
    feature={}
    for w in word_features:
        feature[w] = (w in word)
    return feature


read_pickle = open("pickles/featureset.pickle","rb")
featureset = pickle.load(read_pickle)
read_pickle.close()

training_data = featureset[:10000]
testing_data = featureset[10000:]

read_pickle = open("pickles/gausNB.pickle","rb")
classifier = pickle.load(read_pickle)
read_pickle.close()

read_pickle = open("pickles/MultinomialNB.pickle","rb")
MNB = pickle.load(read_pickle)
read_pickle.close()

read_pickle = open("pickles/BernoulliNB.pickle","rb")
BNB = pickle.load(read_pickle)
read_pickle.close()


vote_classifiers = VotedByClassifiers(BNB,MNB,classifier)

def sentiment(text):
    features = d_features(text)
    return vote_classifiers.classify(features),vote_classifiers.accuracy_level(features)
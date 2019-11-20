import datetime
import nltk
##import tkMessageBox
##from Tkinter import *
import pandas as pd
import numpy as np
import time
##from tkFileDialog import *
import pickle
import re
def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def get_words_in_sentences(sentences):
    all_words = []
    for (words, sentiment) in sentences:
        all_words.extend(words)
    return all_words

def trainSystem():
    print("started")
    train = pd.read_csv("dataset1.csv", header=0, delimiter=",", quoting=1)
    num_reviews = train["statements"].size
    print ("num_reviews",num_reviews)
    p1=(num_reviews*70)//100
    p2=(num_reviews*30)//100
    data = []
    sentiments = []
    global sentences
    sentences = []
    start=0
    stop=p1
    print("start",start,"stop",stop)
    for i in xrange(start, stop):
        sente = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', train["statements"][i])
        sente = re.sub('@[^\s]+', '', sente)
        #every char except alphabets is replaced
        sente=re.sub('[^a-z\s]+',' ',sente,flags=re.IGNORECASE) 

        # Remove additional white spaces
        sente = re.sub('[\s]+', ' ', sente)
        # Replace #word with word
        sente = re.sub(r'#([^\s]+)', r'\1', sente)
        # trim
        sente = sente.strip('\'"')
        words_filtereds = [e.lower() for e in sente.split() if len(e) >= 3]
        sentences.append((words_filtereds, train["Labels"][i]))
    

    word_features = get_word_features(get_words_in_sentences(sentences))

    def extract_features(document):
        document_words = set(document)
        features = {}
        for word in word_features:
            features['contains(%s)' % word] = (word in document_words)
        return features

    print ("sentences",sentences,"\nsentences")
    training_set = nltk.classify.util.apply_features(extract_features, sentences)
    classifier = nltk.NaiveBayesClassifier.train(training_set)
    f = open("instamodelnew.pickle", "wb")
    pickle.dump(classifier, f)
    print ("Training completed")
    classifier.show_most_informative_features(50)
    testing_set = nltk.classify.util.apply_features(extract_features, sentences)

##    testing_set = train["statements"][218:]
##    print("testing_set",testing_set)
    start=p2
    stop=num_reviews
    
    print("start",start,"stop",stop)
    print("Classifier accuracy percent:",nltk.classify.accuracy(classifier,testing_set)*100)
##    print("Classifier accuracy percent:",(nltk.classify.accuracy(classifier, testing_set))*100)
    f.close()

trainSystem()

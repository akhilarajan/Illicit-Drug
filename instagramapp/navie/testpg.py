import datetime
import nltk
import tkMessageBox
from Tkinter import *
import pandas as pd
import numpy as np
import time
from tkFileDialog import *
import pickle

def get_word_features(wordlist):
    wordlist = nltk.FreqDist(wordlist)
    word_features = wordlist.keys()
    return word_features

def get_words_in_sentences(sentences):
    all_words = []
    for (words, sentiment) in sentences:
        all_words.extend(words)
    return all_words

def test_post(txt):
  
    com=txt
    print ("com",com)
    train = pd.read_csv("dataset1.csv", header=0, delimiter=",", quoting=1)
    num_reviews = train["statements"].size
    print (num_reviews)
    sentences = []

    for i in xrange(0, 313):
        # Convert www.* or https?://* to URL
        sente = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', train["statements"][i])
        # Convert @username to AT_USER
        sente = re.sub('@[^\s]+', '', sente)
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

    sents = com
    desicion = ""
    attc = ""
    if len(sents) > 1:
        # Convert to lower case
        # sente = sente_tests.lower()
            sente = re.sub('((www\.[^\s]+)|(https?://[^\s]+))', '', com)
            sente = re.sub('@[^\s]+', '', sente)
            # Remove additional white spaces
            sente = re.sub('[\s]+', ' ', sente)
            # Replace #word with word
            sente = re.sub(r'#([^\s]+)', r'\1', sente)
            # trim
            sente = sente.strip('\'"')
            f = open("instamodelnew.pickle", 'rb')
            classi = pickle.load(f)
            emot = classi.classify(extract_features(sente.split()))
            print (emot)
            desicion = emot
            dic = com + "=" + emot + "\n"

    desicion = desicion.strip()
    print ("Desicion", desicion)
    return desicion

test_post("hello")

import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

wn = WordNetLemmatizer
words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', ',']


class Trainer():
    def __init__(self, file_name):
        self.file_name = file_name

    def get_docs(self):
        intents = json.loads(open(self.file_name).read())

        for intent in intents['intents']:
            for pattern in intent['patterns']:
                word_list = nltk.word_tokenize(pattern)
                words.append(word_list)
                documents.append((word_list, intent['tag']))
                if intent['tag'] not in classes:
                    classes.append(intent['tag'])

        return documents

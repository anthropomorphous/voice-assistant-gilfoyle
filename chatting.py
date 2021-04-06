import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

wn = WordNetLemmatizer()
intents = json.loads(open('intents.json').read())

words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))


def clean_words(text):
    tokenized_text = nltk.word_tokenize(text)
    lemma_text = [wn.lemmatize(word) for word in tokenized_text]
    return lemma_text


def find_the_word(text):
    cleaned_words = clean_words(text)
    bag = [0] * len(words)

    for w in cleaned_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)


def predict_class(model, text):
    loaded_model = load_model(model)
    ftw = find_the_word(text)   # ftw = [0]
    res = loaded_model.predict(np.array([ftw]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)  # sorting by probability in reverse order
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]], 'probability': str(r[1])})

    return return_list


def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break

    return result


class ChatBot():
    def __init__(self, model):
        self.model = model

    def gilfoyle_chatting(self):
        print("Gilfoyle is active now.")
        model_path = 'gilfoyle_chatbot_model_v1.h5'
        while True:
            question = input("")
            ints = predict_class(model_path, question)
            answer = get_response(ints, intents)

            print(answer)

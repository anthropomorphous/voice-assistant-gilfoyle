import os
import random
import json
import pickle
import numpy as np

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

import pyttsx3   # speech synthesis (text-to-speech)
from gtts import gTTS    # yet another text-to-speech from google, works as Google Translator
import playsound

language = 'en'

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
    ftw = find_the_word(text)  # ftw = [0]
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


def speak_gtts(text):
    # Passing the text and language to the engine, here we have marked slow=False. Which tells
    # the module that the converted audio should have a high speed

    response = gTTS(text=text, lang=language, slow=False)
    filename = "voicing_mp3s\\welcome.mp3"
    response.save(filename)
    playsound.playsound(filename)
   # os.system("mpg321 " + "voicing_mp3s\\welcome.mp3")


def speak_pyttsx(text):
    engine = pyttsx3.init(driverName='sapi5')

    """ RATE"""
    rate = engine.getProperty('rate')  # getting details of current speaking rate
    print(rate)  # printing current voice rate
    engine.setProperty('rate', 125)  # setting up new voice rate

    """VOLUME"""
    volume = engine.getProperty('volume')  # getting to know current volume level (min=0 and max=1)
    print(volume)  # printing current volume level
    # engine.setProperty('volume', 0.5)  # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty('voices')  # getting details of current voice
    # engine.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male, 1 for female
    engine.setProperty('voice', voices[1].id)  # changing index, changes voices. 1 for female

    """ Saving Voice to a file
    # On linux make sure that 'espeak' and 'ffmpeg' are installed
    engine.save_to_file('Hello World', 'test.mp3')
    engine.runAndWait()
    """
    engine.say(text)
    engine.runAndWait()


class VoiceBot():
    def __init__(self, model):
        self.model = model

    def gilfoyle_voicing(self):
        print("Gilfoyle is active now.")
        while True:
            question = input("")
            ints = predict_class(self.model, question)
            answer = get_response(ints, intents)
            speak_pyttsx(answer)

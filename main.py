import os
import time
import json
import requests
import datetime

import pyaudio    # microphone usage
import speech_recognition as sr   # (speech-to-text)
import pyttsx3   # speech synthesis (text-to-speech)

import nltk
from nltk.corpus import stopwords

from text_understanding import TextUnderstander
from text_reading import TextReader
from text_parsing import TextParser, get_random_quote
from text_tokenizing_cleaning import TextTokenizerCleaner
from training import Trainer, pickling
from chatting import ChatBot


file_path = "gilfoyle.tsv"
json_file_path = 'intents.json'


def recognize_store_speech(r):
    print('Say something...')
    with sr.Microphone() as source:
        audio = r.listen(source)
    print('I think you\'ve said this: ')
    return audio


if __name__ == '__main__':
    recognizer = sr.Recognizer()

    print('Do you want to recognize your speech?')
    print('Print 0 if you would like to text with me.')
    print('Print 1 to hear the random quote of Gilfoyle.')
    print('Print 2 if speech recognition is needed.')

    numerical_input = int(input())
    if numerical_input == 0:
        print('What is your name?')
        name = str(input())
        txt_und = TextUnderstander(name)
        txt_und.meeter_greeter()

    elif numerical_input == 1:

        txt_rdr = TextReader(str(file_path))
        raw_text = txt_rdr.read_text()
        txt_prsr = TextParser(str(raw_text))
        parsed_df = txt_prsr.parse_tsv_data()
        get_random_quote(parsed_df)
        """
        txt_cleaner = TextTokenizerCleaner(parsed_df)
        df = txt_cleaner.preprocess_df()
        print(df.head())
        """
        trainer = Trainer(str(json_file_path))
        documents, words, classes = trainer.get_docs()
        pickling(words, classes)
        #model = trainer.training(documents, words, classes)
        model = 'gilfoyle_chatbot_model_v1.h5'
        cb = ChatBot(str(model))
        cb.gilfoyle_chatting()


    else:
        while(True):
            voice_input = recognize_store_speech(recognizer)

            try:
                print("Gilfoyle thinks you said: \"{0}\" ".format(recognizer.recognize_google(voice_input)))
            except sr.UnknownValueError:
                print("Gilfoyle could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

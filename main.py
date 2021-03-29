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

# import wikipedia
# import webbrowser
# import subprocess
# from ecapture import ecapture as ec
# import wolframalpha
# import requests


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
    print('Print 1 to hear the quote of Gilfoyle.')
    print('Print 2 if speech recognition is needed.')

    numerical_input = int(input())
    if numerical_input == 0:
        print('What is your name?')
        name = str(input())
        txt_und = TextUnderstander(name)
        txt_und.meeter_greeter()

    elif numerical_input == 1:
        file_path = "gilfoyle.tsv"
        txt_rdr = TextReader(str(file_path))
        txt_rdr.print_file()

    else:
        while(True):
            voice_input = recognize_store_speech(recognizer)

            # recognize speech using Google Speech Recognition
            try:
                # for testing purposes, we're just using the default API key
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                # instead of `r.recognize_google(audio)`

                print("Gilfoyle thinks you said: \"{0}\" ".format(recognizer.recognize_google(voice_input)))
            except sr.UnknownValueError:
                print("Gilfoyle could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

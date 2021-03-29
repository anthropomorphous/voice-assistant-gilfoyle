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
    print('Print 0 if you would like to text with me. Print 1 if speech recognition is needed.')

    numerical_input = int(input())
    if numerical_input == 0:
        print('What is your name?')
        name = str(input())
        fowl = TextUnderstander(name)
        fowl.meeter_greeter()

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

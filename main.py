import os
import time
import json
import requests
import datetime

import pyaudio    #microphone usage
import speech_recognition as sr
import pyttsx3   #speech synthesis
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

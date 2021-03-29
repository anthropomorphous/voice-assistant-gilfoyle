import nltk
from nltk.corpus import stopwords


class TextUnderstander():
    def __init__(self, input_name):
        self.hidden_name = input_name

    def get_name(self):
        return self.hidden_name

    def set_name(self, input_name):
        self.hidden_name = input_name

    name = property(get_name, set_name)

    def meeter_greeter(self):
        print('Welcome back, {0}, son of the b*tch.'.format(self.name))

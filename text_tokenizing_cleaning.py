import string
import re
import pandas as pd
import nltk

pd.set_option('display.max_colwidth', 100)


# Remove punctuation
def remove_punct(text):
    text_no_punct = "".join([char for char in text if char not in string.punctuation])
    return text_no_punct


# Tokenization
def tokenize(text):
    tokens = re.split('\W+', text)
    return tokens


# Remove stopwords (I, my, and, but etc)
def remove_stpw(token_list):
    stopwords = nltk.corpus.stopwords.words('english')
    text = [word for word in token_list if word not in stopwords]
    return text


class TextTokenizerCleaner():
    def __init__(self, input_df):
        self.hidden_df = input_df

    def get_data(self):
        return self.hidden_df

    def set_data(self, input_df):
        self.hidden_df = input_df

    data = property(get_data, set_data)

    def preprocess_df(self):
        self.data['cleaned_question'] = self.data['question'].apply(lambda x: remove_punct(x))
        self.data['cleaned_answer'] = self.data['answer'].apply(lambda x: remove_punct(x))

        self.data['tokenized_question'] = self.data['cleaned_question'].apply(lambda x: tokenize(x.lower()))
        self.data['tokenized_answer'] = self.data['cleaned_answer'].apply(lambda x: tokenize(x.lower()))

        self.data['question_nostop'] = self.data['tokenized_question'].apply(lambda x: remove_stpw(x))
        self.data['answer_nostop'] = self.data['tokenized_answer'].apply(lambda x: remove_stpw(x))

        prepared_df = self.data
        return prepared_df

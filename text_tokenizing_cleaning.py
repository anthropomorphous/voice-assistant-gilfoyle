import string
import re
import pandas as pd
import nltk
#nltk.download('wordnet')
from sklearn.feature_extraction.text import CountVectorizer

pd.set_option('display.max_colwidth', 100)
ps = nltk.PorterStemmer()
wn = nltk.WordNetLemmatizer()

"""
 In the next episode:
Feature Engineering - Sentiment analysis, topic modeling, named-entity recognition
"""

# Removes punctuation, tokenizes text, removes stopwords (i, my, and)
def clean_text(text):
    text_no_punct = "".join([char for char in text if char not in string.punctuation])
    tokens = re.split('\W+', text_no_punct)
    stopwords = nltk.corpus.stopwords.words('english')
    text = [word for word in tokens if word not in stopwords]
    return text


# Stemming words (reduce corpus of words, stemming -> stem etc)
def stemming(tokenized_text):
    text = [ps.stem(word) for word in tokenized_text]
    return text


def lemmatizing(tokenized_text):
    text = [wn.lemmatize(word) for word in tokenized_text]
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
        self.data['question_clean'] = self.data['question'].apply(lambda x: clean_text(x.lower()))
        self.data['answer_clean'] = self.data['answer'].apply(lambda x: clean_text(x.lower()))

        self.data['question_stemmed'] = self.data['question_clean'].apply(lambda x: stemming(x))
        self.data['answer_stemmed'] = self.data['answer_clean'].apply(lambda x: stemming(x))

       # self.data['question_lemmatized'] = self.data['question_clean'].apply(lambda x: lemmatizing(x))
       # self.data['answer_lemmatized'] = self.data['answer_clean'].apply(lambda x: lemmatizing(x))

        prepared_df = self.data
        return prepared_df

import string
import re
import pandas as pd
import nltk
#nltk.download('wordnet')
from sklearn.feature_extraction.text import CountVectorizer

pd.set_option('display.max_colwidth', 100)
ps = nltk.PorterStemmer()
wn = nltk.WordNetLemmatizer()
ignore_punct = ['?', '!', '.', ',']


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


#def preprocess_lists(words):
    #for word in words:
    #    word = [x.lower() for x in word]
    #words_cleaned = [clean_text(words) for x in words]
    #words_lemmatized = [wn.lemmatize(x) for x in words if x not in ignore_punct]

    #return words_lemmatized


class TextTokenizerCleaner():
    def __init__(self, dataframe):
        self.dataframe = dataframe

    def preprocess_df(self):
        self.dataframe['question_clean'] = self.dataframe['question'].apply(lambda x: clean_text(x.lower()))
        self.dataframe['answer_clean'] = self.dataframe['answer'].apply(lambda x: clean_text(x.lower()))

        self.dataframe['question_stemmed'] = self.dataframe['question_clean'].apply(lambda x: stemming(x))
        self.dataframe['answer_stemmed'] = self.dataframe['answer_clean'].apply(lambda x: stemming(x))

       # self.data['question_lemmatized'] = self.data['question_clean'].apply(lambda x: lemmatizing(x))
       # self.data['answer_lemmatized'] = self.data['answer_clean'].apply(lambda x: lemmatizing(x))

        prepared_df = self.dataframe
        return prepared_df

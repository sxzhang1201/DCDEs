from nltk.corpus import stopwords
import nltk

default_stopwords = nltk.corpus.stopwords.words('english')

extra_stopwords = ["yes", "please"]

stopwords = default_stopwords + extra_stopwords


def remove_stopwords(token_list):
    token_list = [w for w in token_list if w not in stopwords]

    return token_list



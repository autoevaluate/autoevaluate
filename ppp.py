import nltk
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import requests
import json
import string
from math import sqrt
from collections import Counter
from itertools import chain
from functools import reduce
from transformers import AutoTokenizer, AutoModel
import numpy as np
# from c.models.keyedvectors import KeyedVectors 
import math
from werkzeug.wrappers import Request, Response
from sklearn.feature_extraction.text import TfidfVectorizer,CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


from math import sqrt
from collections import Counter
def pre_process(answer):
    # text=answer.read().decode()
    # Case folding
    text=answer
    text = text.lower()
    
    # Tokenization
    tokens = word_tokenize(text)
    
    # Removing stop words
    stop_words = set(stopwords.words("english"))
    tokens = [token for token in tokens if token.lower() not in stop_words]
    
    # Removing punctuation and special characters
    table = str.maketrans('', '', string.punctuation)
    stripped = [token.translate(table) for token in tokens]
    stripped = [token for token in stripped if token.isalpha() or token.isdigit()]
    
    return stripped

fle=open("F:/Final Year Project - Copy - Copy - Copy/test1.txt",'r')
flee=open("F:/Final Year Project - Copy - Copy - Copy/test2.txt",'r')
cont=fle.read()
con=flee.read()

from gensim import corpora, models
from gensim.similarities import Similarity

def calculate_cosine_similarity(text1,text2,marks):
    # tokenize and create a dictionary of words
    texts = [text1, text2]
    dictionary = corpora.Dictionary(texts)

    # convert texts into vectors using Bag of Words model
    corpus = [dictionary.doc2bow(text) for text in texts]

    # train the LSI model on the corpus
    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)

    # convert the texts into LSI vectors
    text1_lsi = lsi[dictionary.doc2bow(text1)]
    text2_lsi = lsi[dictionary.doc2bow(text2)]

    # compute similarity score using cosine similarity of LSI vectors
    similarity_score = Similarity('', corpus=lsi[corpus], num_features=2)[text1_lsi][1]
    return (similarity_score*marks)



bb=pre_process(con)

aa=pre_process(cont)
print(calculate_cosine_similarity(aa,bb,20))




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

import numpy as np
# from c.models.keyedvectors import KeyedVectors 
import math
from werkzeug.wrappers import Request, Response



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
    if 'logged_in' in session:
        return stripped
    else:
        return redirect(url_for('login'))


def check_grammar(text):
    url = 'https://languagetool.org/api/v2/check'
    data = {
        'text': text,
        'language': 'en-US'
    }
    response = requests.post(url, data=data)
    result = response.json()
    errors = result['matches']
    no_of_errors = len(errors)
    if no_of_errors>100:
        g=0
    elif no_of_errors>=90 and no_of_errors<=100:
        g=0.1
    elif no_of_errors>=80 and no_of_errors<90:
        g=0.2
    elif no_of_errors>=70 and no_of_errors<80:
        g=0.3
    elif no_of_errors>=60 and no_of_errors<70:
        g=0.4
    elif no_of_errors>=50 and no_of_errors<60:
        g=0.5
    elif no_of_errors>=40 and no_of_errors<50:
        g=0.6
    elif no_of_errors>=30 and no_of_errors<40:
        g=0.7
    elif no_of_errors>=20 and no_of_errors<30:
        g=0.8
    elif no_of_errors>=10 and no_of_errors<20:
        g=0.9
    else:
        g=1
    return str(g)
    if 'logged_in' in session:
        return str(g)
    else:
        return redirect(url_for('login'))


#length of string
def CheckLenght(client_answer):
    
    client_ans = len(client_answer.split())
    #return client_ans
    kval1 = 0
    if client_ans > 50:
        kval1 = 1
    elif client_ans > 40:
        kval1 = 2
    elif client_ans > 30:
        kval1 = 3
    elif client_ans > 20:
        kval1 = 4
    elif client_ans > 10:
        kval1 = 5
    else:
        kval1 = 6
    # return str(kval1)
    # if 'logged_in' in session:
    #     return str(kval1)
    # else:
    #     return redirect(url_for('login'))


def cosine_similarity(words1, words2):
    word_set = set(words1).union(set(words2))
    word_dict1 = Counter(words1)
    word_dict2 = Counter(words2)
    numerator = reduce(lambda x, y: x + y, map(lambda w: word_dict1[w] * word_dict2[w], word_set))
    denominator1 = sqrt(reduce(lambda x, y: x + y, map(lambda w: word_dict1[w]**2, word_dict1.keys())))
    denominator2 = sqrt(reduce(lambda x, y: x + y, map(lambda w: word_dict2[w]**2, word_dict2.keys())))
    denominator = denominator1 * denominator2
    # if not denominator:
    #     return 0.0
    # else:
    #     return float(numerator) / denominator


def main(answer,answer_key):
    source_doc1=answer
    target_docs=answer_key
    key_length=CheckLenght(answer)
    key_Error=check_grammar(answer_key)
    pre_proce_answer=pre_process(answer)
    pre_proce_answer_key=pre_process(answer_key)
    key_match=cosine_similarity(pre_proce_answer,pre_proce_answer)
    # sim_scores = ds.calculate_similarity(source_doc1, target_docs)
    # marks2 =  ((sum(sim_scores) / len(sim_scores)) * 60)+ (10/key_match) + (20 * key_Error) + (10/key_length)
    # return str(mark2)
    return str(key_match)
    

    

# with open("CaseFolding.txt", "r") as file:
#     text = file.read()
#     pre_processed_text = pre_process(text)
#     print(pre_processed_text)

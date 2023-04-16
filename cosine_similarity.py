import string
from math import sqrt
from collections import Counter
from itertools import chain
from functools import reduce

# function to read a text file and return a list of words
def read_file(file_path):
    with open(file_path, 'r') as file:
        text = file.read().lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        words = text.split()
        return words

# function to compute the cosine similarity between two lists of words
def cosine_similarity(words1, words2):
    word_set = set(words1).union(set(words2))
    word_dict1 = Counter(words1)
    word_dict2 = Counter(words2)
    numerator = reduce(lambda x, y: x + y, map(lambda w: word_dict1[w] * word_dict2[w], word_set))
    denominator1 = sqrt(reduce(lambda x, y: x + y, map(lambda w: word_dict1[w]**2, word_dict1.keys())))
    denominator2 = sqrt(reduce(lambda x, y: x + y, map(lambda w: word_dict2[w]**2, word_dict2.keys())))
    denominator = denominator1 * denominator2
    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

# example usage
file1 = "test1.txt"
file2 = "test2.txt"

words1 = read_file(file1)
words2 = read_file(file2)

similarity = cosine_similarity(words1, words2)
print(f"Cosine similarity between {file1} and {file2}: {similarity}")

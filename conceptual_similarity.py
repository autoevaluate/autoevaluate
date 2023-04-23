import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

# def calculate_cosine_similarity(doc1, doc2):
#     # Create CountVectorizer object to convert text to numerical representations
#     vectorizer = CountVectorizer()

#     # Fit and transform the input documents
#     doc1_vector = vectorizer.fit_transform([doc1])
#     doc2_vector = vectorizer.transform([doc2])

#     # Compute cosine similarity between the transformed documents
#     similarity = cosine_similarity(doc1_vector, doc2_vector)

#     return similarity[0][0]









from gensim import corpora, models
from gensim.similarities import Similarity

def calculate_cosine_similarity(text1,text2):
    # tokenize and create a dictionary of words
    texts = [text1.split(), text2.split()]
    dictionary = corpora.Dictionary(texts)

    # convert texts into vectors using Bag of Words model
    corpus = [dictionary.doc2bow(text) for text in texts]

    # train the LSI model on the corpus
    lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)

    # convert the texts into LSI vectors
    text1_lsi = lsi[dictionary.doc2bow(text1.split())]
    text2_lsi = lsi[dictionary.doc2bow(text2.split())]

    # compute similarity score using cosine similarity of LSI vectors
    similarity_score = Similarity('', corpus=lsi[corpus], num_features=2)[text1_lsi][1]
    return (similarity_score)











# Example usage
file1_path = 'test1.txt'
file2_path = 'test2.txt'

# Read content from text files
doc1 = read_text_file(file1_path)
doc2 = read_text_file(file2_path)

# Calculate cosine similarity
similarity = calculate_cosine_similarity(doc1, doc2)
print("Conceptual similarity between", file1_path, "and", file2_path, ":", similarity)

import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return content

def calculate_cosine_similarity(doc1, doc2):
    # Create CountVectorizer object to convert text to numerical representations
    vectorizer = CountVectorizer()

    # Fit and transform the input documents
    doc1_vector = vectorizer.fit_transform([doc1])
    doc2_vector = vectorizer.transform([doc2])

    # Compute cosine similarity between the transformed documents
    similarity = cosine_similarity(doc1_vector, doc2_vector)

    return similarity[0][0]

# Example usage
file1_path = 'test1.txt'
file2_path = 'test2.txt'

# Read content from text files
doc1 = read_text_file(file1_path)
doc2 = read_text_file(file2_path)

# Calculate cosine similarity
similarity = calculate_cosine_similarity(doc1, doc2)
print("Conceptual similarity between", file1_path, "and", file2_path, ":", similarity)

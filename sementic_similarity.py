from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def sementgic_similarity(text1,text2):

    # Tokenize and preprocess texts
    text1_tokens = text1.split()
    text2_tokens = text2.split()

    # Combine tokens into sentences
    text1_sentences = [' '.join(text1_tokens)]
    text2_sentences = [' '.join(text2_tokens)]

    # Create TfidfVectorizer instance
    vectorizer = TfidfVectorizer()

    # Fit and transform the text data
    tfidf_matrix = vectorizer.fit_transform(text1_sentences + text2_sentences)

    # Extract the feature vectors for the two texts
    text1_vector = tfidf_matrix[0]
    text2_vector = tfidf_matrix[1]

    # Calculate cosine similarity
    similarity_score = cosine_similarity(text1_vector, text2_vector)
    return ("Sementic Similarity Score:", similarity_score[0][0])



    
fle=open("F:/Final Year Project - Copy - Copy - Copy/test1.txt",'r')
flee=open("F:/Final Year Project - Copy - Copy - Copy/test2.txt",'r')
cont=fle.read()
con=flee.read()
print(sementgic_similarity(cont,con))
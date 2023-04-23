# Keywords  matching

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def KeyWordmatching(text1, text2):
    # Create a CountVectorizer object to tokenize the text
    vectorizer = CountVectorizer()

    # Fit the CountVectorizer object to the text and transform the text into a document-term matrix
    dtm = vectorizer.fit_transform([text1, text2])

    # Calculate the cosine similarity between the two rows of the document-term matrix
    cosine_sim = cosine_similarity(dtm)[0][1]

    # Calculate the number of matching keywords as the cosine similarity multiplied by the total number of unique words
    num_matching_keywords = round(cosine_sim * len(set(text1.split() + text2.split())))

    value=num_matching_keywords
    
    return num_matching_keywords

    
fle=open("F:/Final Year Project - Copy - Copy - Copy/test1.txt",'r')
flee=open("F:/Final Year Project - Copy - Copy - Copy/test2.txt",'r')
cont=fle.read()
con=flee.read()

# change the variables
print(KeyWordmatching(cont,con))

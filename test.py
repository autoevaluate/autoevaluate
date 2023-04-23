import spacy

# load the pre-trained model
nlp = spacy.load('en_core_web_md')

# define two texts
text1 = nlp('blue car')
text2 = nlp('red car')

# compute similarity score using cosine similarity of sentence vectors
similarity_score = text1.similarity(text2)
print(similarity_score)

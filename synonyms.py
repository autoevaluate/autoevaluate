import requests

# Function to get synonyms using Datamuse API
def get_synonyms(word):
    base_url = "https://api.datamuse.com/words"
    params = {
        "rel_syn": word
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    synonyms = [result["word"] for result in data]
    return synonyms


fle=open("F:/Final Year Project - Copy - Copy - Copy/test1.txt",'r')
flee=open("F:/Final Year Project - Copy - Copy - Copy/test2.txt",'r')
cont=fle.read()
con=flee.read()
text1=cont
text2=con

# Tokenize and preprocess words in text1 and text2
text1_words = set(text1.split())
text2_words = set(text2.split())

# Find synonyms from text1 that are present in text2
common_synonyms = set()
for word in text1_words:
    synonyms = get_synonyms(word)
    for synonym in synonyms:
        if synonym in text2_words:
            common_synonyms.add(synonym)

# Print the synonyms found in text2
print("Synonyms found in text2:")
print(", ".join(common_synonyms))

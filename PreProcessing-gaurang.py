import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

def pre_process(text):
    # Case folding
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

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in stripped]

    return lemmatized_tokens

with open("CaseFolding.txt", "r") as file:
    text = file.read()
    pre_processed_text = pre_process(text)
    print(pre_processed_text)


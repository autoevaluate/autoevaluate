# contraduction

from transformers import AutoTokenizer, AutoModel

# Load pre-trained BERT model and tokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-cased')
model = AutoModel.from_pretrained('bert-base-cased')

text1 = "The earth is flat."
text2 = "helo"

# Encode the two texts using the tokenizer and pass the resulting tensors to the model
encoded_text1 = tokenizer(text1, return_tensors='pt')
encoded_text2 = tokenizer(text2, return_tensors='pt')

# Get the model outputs for the encoded texts
outputs1 = model(**encoded_text1)
outputs2 = model(**encoded_text2)

# Compare the encoded vectors of the two texts using cosine similarity
from torch.nn import CosineSimilarity
cos_sim = CosineSimilarity(dim=1, eps=1e-6)
similarity = cos_sim(outputs1.last_hidden_state.mean(dim=1), outputs2.last_hidden_state.mean(dim=1))

if similarity < 0.8:
    print("There is a contradiction.")
else:
    print("There is no contradiction.")

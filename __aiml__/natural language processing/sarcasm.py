import json

with open("sarcasm.json", 'r') as f:
	datastore = json.load(f)

# non-sarcastic headline
print(datastore[0])
print()
# sarcastic headline
print(datastore[20000])
print()
sentences = []
labels = []
urls = []

for item in datastore:
	sentences.append(item['headline'])
	labels.append(item['is_sarcastic'])
	urls.append(item['article_link'])

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# initializing tokenizer
tokenizer = Tokenizer(oov_token='<OOV>')

# generate the word index dictionary
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

# Generate the pad sequences
sequences = tokenizer.texts_to_sequences(sentences)
padded = pad_sequences(sequences, padding='post')

print(f'sample headline: {sentences[2]}')
print(f'padded sequence: {padded[0]}')
print(f'shape of the padded sequencce: {padded.shape}')
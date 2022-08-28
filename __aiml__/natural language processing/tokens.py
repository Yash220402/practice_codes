from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

sentences = [
	"I love my dog",
	"I love my cat",
	"You love my dog!",
	"Do you think my dog is amazing?"
]

tokenizer = Tokenizer(num_words = 100, oov_token="<OOV>")
tokenizer.fit_on_texts(sentences)
word_index = tokenizer.word_index

sequences = tokenizer.texts_to_sequences(sentences)

padded = pad_sequences(sequences)
print("\nWord index =", word_index)
print("\nSequences =", sequences)

# Padding the sequences
padded = pad_sequences(sequences, padding="post", truncating="post", maxlen=5)
print("\nPadded Sequences:")
print(padded)

test_data = [
	'i really love my dog',
	'my dog loves my manatee'
]

test_seq = tokenizer.texts_to_sequences(test_data)
print("\nTest Sequence =", test_seq)

test_padded = pad_sequences(test_seq, padding="post", truncating="post", maxlen=5)
print("Padded test sequence:")
print(test_padded)
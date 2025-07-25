import nltk
nltk.download('punkt')
nltk.download('all')  # Optional: download everything to avoid such issues again


from nltk.tokenize import word_tokenize

text = "India launched Chandrayaan-3."
tokens = word_tokenize(text)
print(tokens)

# Whitespace Tokenizer

def WhitesapceTokenizer(str):
    words = str.split(" ")
    return words


sentence = "I can't believe it's 3.14!"
tokens = WhitesapceTokenizer(sentence)

print(tokens)
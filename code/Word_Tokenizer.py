import re


class WordTokenizer():
    def __init__(self):
        self.contractions = re.compile(r"(?i)\b(can't|won't|n't|'ll|'re|'ve|'s|'m)\b")
        self.punctuation = re.compile(r"([.,!?():;])")  # Separates common punctuation
        self.double_quotes = re.compile(r'``|\'\'')     # Handles double quotes
        self.starting_quotes = re.compile(r'^\"')       # Handles starting quotes
        self.ending_quotes = re.compile(r'\"$')         # Handles ending quotes

    def tokenize(self, text):
        # Handle double quotes
        text = self.double_quotes.sub('"', text)

        # Separate punctuation
        text = self.punctuation.sub(r' \1 ', text)

        # Split contractions
        text = self.contractions.sub(r' \1', text)

        # Normalize spaces
        tokens = text.strip().split()
        return tokens
    


tokenzier = WordTokenizer()
sentence = "I can't believe it's 3.14!"

tokens = tokenzier.tokenize(sentence)
print(tokens)
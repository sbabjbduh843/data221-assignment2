import string
from collections import Counter

with open('sample-file.txt', 'r') as l:
    text = l.read()

tokens = text.split()

tokens = [token.lower() for token in tokens]

cleaned_tokens = []

for token in tokens:
    cleaned_token = token.strip(string.punctuation)
    cleaned_tokens.append(cleaned_token)

tokens = cleaned_tokens

filtered_tokens = []

for token in tokens:
    letter_count = sum(c.isalpha() for c in token)
    if letter_count >= 2:
        filtered_tokens.append(token)

tokens = filtered_tokens

word_counts = Counter(tokens)
top_10 = word_counts.most_common(10)
for word, count in top_10:
    print(f"{word} -> {count}")


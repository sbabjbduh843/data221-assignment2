import string
from collections import Counter

with open("sample-file.txt", "r", encoding="utf-8") as f:
    text = f.read()

tokens = text.split()

tokens = [token.lower() for token in tokens]

cleaned_tokens = []
for token in tokens:
    cleaned_tokens.append(token.strip(string.punctuation))

tokens = cleaned_tokens

filtered_tokens = []
for token in tokens:
    if sum(c.isalpha() for c in token) >= 2:
        filtered_tokens.append(token)

tokens = filtered_tokens

bigrams = []
for i in range(len(tokens) - 1):
    bigrams.append((tokens[i], tokens[i + 1]))

bigram_counts = Counter(bigrams)

top_5 = bigram_counts.most_common(5)

for (word1, word2), count in top_5:
    print(f"{word1} {word2} -> {count}")

import re
import string
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from collections import Counter

customer_comments = [
    "I love this product! It's amazing and easy to use.",
    "The customer service is terrible. Worst experience ever.",
    "This is a great product, but the delivery was delayed.",
    "Highly recommended! Quality is top-notch.",
    "The product didn't meet my expectations. Disappointing.",
    "Fantastic product! Worth every penny.",
    "Terrible customer support. I'll never buy from them again.",
    "Great value for money. Exceeded my expectations.",
    "The product is good, but the website needs improvement.",
    "Excellent product and service. Will definitely buy again."
]

def preprocess_text(text):
    text = re.sub(r'[%s]' % re.escape(string.punctuation), '', text)
    text = text.lower()
    stop_words = set(stopwords.words('english'))
    text = ' '.join([word for word in text.split() if word not in stop_words])
    return text

preprocessed_comments = [preprocess_text(comment) for comment in customer_comments]

tokenized_comments = [comment.split() for comment in preprocessed_comments]
tokenized_comments = [token for comment in tokenized_comments for token in comment]

word_freq = Counter(tokenized_comments)

N = int(input("Enter the number of top frequent words to display: "))

print(f"Top {N} most frequent words:")
for word, freq in word_freq.most_common(N):
    print(f"{word}: {freq}")

top_words = [word for word, _ in word_freq.most_common(N)]
top_freqs = [freq for _, freq in word_freq.most_common(N)]

plt.figure(figsize=(10, 6))
plt.bar(top_words, top_freqs)
plt.xticks(rotation=45)
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.title('Top N Most Frequent Words')
plt.show()

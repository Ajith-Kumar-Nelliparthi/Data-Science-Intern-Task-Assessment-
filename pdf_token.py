import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
import string
from nltk import FreqDist

# Ensure you have the necessary NLTK resources
nltk.download('punkt')
nltk.download('punkt_tab')  # Download punkt_tab if missing
nltk.download('stopwords')

# Read the extracted text from the file with a different encoding
try:
    with open('extracted_text.txt', 'r', encoding='utf-8') as txt:
        text = txt.read()
except UnicodeDecodeError:
    # If UTF-8 fails, try reading with 'latin-1' encoding
    with open('extracted_text.txt', 'r', encoding='latin-1') as txt:
        text = txt.read()

# Tokenization
word_tokens = word_tokenize(text)
sentence_tokens = sent_tokenize(text)

# Cleaning tokens: Remove stop words and punctuation
stop_words = set(stopwords.words('english'))
cleaned_tokens = [word for word in word_tokens if word.lower() not in stop_words and word not in string.punctuation]

# Frequency distribution
word_frequencies = FreqDist(cleaned_tokens)
sorted_frequencies = sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True)

# Summary of tokenized words
print("Word Frequency Summary:")
for word, frequency in sorted_frequencies:
    print(f"{word}: {frequency}")
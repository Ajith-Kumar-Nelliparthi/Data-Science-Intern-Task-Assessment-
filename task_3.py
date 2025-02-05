# sentiment analysis
# import libraries
import nltk # Natural Language Toolkit
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

# initalize sentiment analyzer
std = SentimentIntensityAnalyzer()

sample_texts = [
    "I love this product! It's amazing!",
    "Terrible service. Would not recommend.",
    "It's okay, not great but not bad either.",
    "The item arrived damaged. Very disappointed.",
    "Absolutely fantastic experience!"
]

sentiment_counts = {'positive':0,'negative':0,'neutral':0}

for text in sample_texts:
    score = std.polarity_scores(text)
    compound_score = score['compound']
    if compound_score >= 0.05:
        sentiment = 'positive'
    elif compound_score <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    sentiment_counts[sentiment] += 1

total = len(sample_texts)
distribution = {
    "positive": f"{(sentiment_counts['positive'] / total) * 100:.1f}%",
    "neutral": f"{(sentiment_counts['neutral'] / total) * 100:.1f}%",
    "negative": f"{(sentiment_counts['negative'] / total) * 100:.1f}%"
}

print(distribution)
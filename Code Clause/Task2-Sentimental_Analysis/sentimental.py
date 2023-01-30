import nltk
from nltk.sentiment import SentimentIntensityAnalyzer


def get_sentiment(text):
    nltk.download('vader_lexicon')
    sid = SentimentIntensityAnalyzer()
    sentiment = sid.polarity_scores(text)
    if sentiment['compound'] >= 0.05:
        return "positive"
    elif sentiment['compound'] <= -0.05:
        return "negative"
    else:
        return "neutral"


text = "This is an amazing product! I love it so much."
print(get_sentiment(text))  # Output: "positive"

text = "This product is terrible. I would not recommend it."
print(get_sentiment(text))  # Output: "negative"

import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("reviews.csv")

# Function to analyze sentiment
def get_sentiment(text):
    analysis = TextBlob(text)

    if analysis.sentiment.polarity > 0:
        return "Positive"
    elif analysis.sentiment.polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment analysis
data["Sentiment"] = data["review"].apply(get_sentiment)

# Show results
print(data)

# Count sentiment
sentiment_counts = data["Sentiment"].value_counts()

# Visualization
sns.countplot(x="Sentiment", data=data)

plt.title("Sentiment Analysis Result")
plt.show()
# sentiment_model.py - Dynamic placeholder sentiment analysis

def get_sentiment(text):
    """
    Returns a basic sentiment analysis based on keywords.
    Positive, Neutral, Negative sentiment with a score between 0 and 1.
    """
    text_lower = text.lower()

    # Define simple keyword-based scoring
    positive_keywords = ["ai", "innovative", "smart", "efficient", "personalized", "improve", "growth"]
    negative_keywords = ["problem", "risk", "challenge", "expensive", "dependency", "data required"]

    pos_score = sum([1 for word in positive_keywords if word in text_lower])
    neg_score = sum([1 for word in negative_keywords if word in text_lower])

    # Calculate final score (0 to 1)
    score = max(min((pos_score - neg_score) * 0.2 + 0.5, 1), 0)  # Center at 0.5

    if score > 0.6:
        sentiment = "Positive"
    elif score < 0.4:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {"sentiment": sentiment, "score": score}

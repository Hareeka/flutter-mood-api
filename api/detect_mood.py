from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from flask import Request, jsonify

def handler(request: Request):
    request_json = request.get_json()
    text = request_json.get('text', '')
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    
    mood = "Calm"
    if score['compound'] >= 0.5:
        mood = "Happy"
    elif score['compound'] <= -0.5:
        mood = "Sad"
    elif score['compound'] < 0 and score['compound'] > -0.5:
        mood = "Stressed"
    
    return jsonify({"mood": mood, "score": score})



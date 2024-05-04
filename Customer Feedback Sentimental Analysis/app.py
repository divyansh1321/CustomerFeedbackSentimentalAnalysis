from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    feedback = request.form['feedback']
    sentiment = analyze_sentiment(feedback)
    word_count = count_words(feedback)
    char_count = count_characters(feedback)
    polarity = calculate_polarity(feedback)
    return render_template('result.html', feedback=feedback, sentiment=sentiment,
                           word_count=word_count, char_count=char_count, polarity=polarity)

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return 'Positive 😊'
    elif polarity < 0:
        return 'Negative 😔'
    else:
        return 'Neutral 😐'

def count_words(text):
    return len(text.split())

def count_characters(text):
    return len(text)

def calculate_polarity(text):
    return TextBlob(text).sentiment.polarity

if __name__ == '__main__':
    app.run(debug=True)

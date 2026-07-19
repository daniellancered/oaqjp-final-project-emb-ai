"""
Emotion Detection Web Application.

This module provides a Flask-based web interface for running sentiment and
emotion analysis on user-provided text inputs via an external API.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Route to analyze the query text and return formatted emotion scores.
    
    Returns:
        str: A formatted string showing emotion breakdown or an error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    output = emotion_detector(text_to_analyze)

    if output['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    return (
        f"For the given statement, the system response is "
        f"'anger': {output['anger']}, 'disgust': {output['disgust']}, "
        f"'fear': {output['fear']}, 'joy': {output['joy']} and "
        f"'sadness': {output['sadness']}. "
        f"The dominant emotion is {output['dominant_emotion']}."
    )


@app.route("/")
def home():
    """
    Route to serve the landing page of the application.
    
    Returns:
        Response: The rendered index.html template.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    
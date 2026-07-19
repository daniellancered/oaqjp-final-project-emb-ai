from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector
app = Flask("__main__")


@app.route("/emotionDetector")
def emotion_detector_route():
    text_to_analyze = request.args.get("textToAnalyze")
    output = emotion_detector(text_to_analyze)
    if output['dominant_emotion'] is None:
        return "Invalid text! Please try again!."
    return f"For the given statement, the system response is 'anger': {output['anger']}, 'disgust': {output['disgust']}, 'fear': {output['fear']}, 'joy': {output['joy']} and 'sadness': {output['sadness']}. The dominant emotion is {output['dominant_emotion']}."

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000)
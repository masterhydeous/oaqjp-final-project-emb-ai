'''
invoke analysis method
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def sent_analyzer():
    '''invoke analysis method'''

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')

    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    # Extract the label and score from the response
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    if dominant_emotion  is None:
        return "Invalid text! Please Try again."

    # Return a formatted string with the sentiment label and score
    return f"For the given statement, the system response is \
     'anger':{anger},disgust':{disgust},'fear':{fear},'joy':{joy},'sadness':{sadness}. \
     The dominant emotion is {dominant_emotion}"

@app.route("/")
def render_index_page():
    '''invoke analysis method'''

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

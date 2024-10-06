"""This module provides a Flask web application for emotion detection.

The application processes input text and returns emotions detected
along with their respective scores.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """Render the home page."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_route():
    """Handle the emotion detection request.

    Returns:
        JSON response with emotion analysis results or an error message.
    """
    data = request.get_json()

    # Check if data is provided
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400

    text_to_analyze = data.get('text', '')

    # Check if the text is empty
    if not text_to_analyze.strip():
        return jsonify({'error': 'Invalid text! Please try again.'}), 400

    try:
        # Call the emotion_detector function
        emotion_results = emotion_detector(text_to_analyze)

        # Check if emotion detection was successful
        if not emotion_results or 'dominant_emotion' not in emotion_results:
            return jsonify({'error': 'Could not detect emotion! Please try again.'}), 500

        # Prepare the response format
        response_text = {
            'anger': emotion_results['anger'],
            'disgust': emotion_results['disgust'],
            'fear': emotion_results['fear'],
            'joy': emotion_results['joy'],
            'sadness': emotion_results['sadness'],
            'dominant_emotion': emotion_results['dominant_emotion']
        }

        return jsonify(response_text), 200

    except (KeyError, TypeError) as e:  # Catch specific exceptions
        # Handle specific exceptions and return error message
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

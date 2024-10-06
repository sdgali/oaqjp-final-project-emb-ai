import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():
        # Return None for all keys if the input is blank
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Correct URL for the API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Create a dictionary with the text to be analyzed
    input_json = { "raw_document": { "text": text_to_analyze } }

    # Correct headers with the appropriate model ID
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the sentiment analysis API
    response = requests.post(url, json=input_json, headers=headers)

    # Check if response is successful
    if response.status_code == 400:
        # Return None for all keys if the API responds with a bad request
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting emotion scores from the response
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Finding the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    # Returning the results
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }

import requests
import json

def emotion_detector(text_to_analyse):
    



    # URL for the Watson Emotion Predict API
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Headers for the API request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # JSON input format for the request
    data = {
        "raw_document": {
            "text": text_to_analyse
        }
    }
    
    # Sending a POST request to the API
    response = requests.post(url, json=data, headers=headers)
    
    # Handling the response
    if response.status_code == 200:
        # Print the full response for debugging
        print("Response from API:", response.text)
        
        # Parsing the JSON response
        formatted_response = json.loads(response.text)
        
        # Check the structure of the response and extract emotions
        try:
            # Access the emotions from the correct key
            emotions = formatted_response['emotionPredictions'][0]['emotion']
            # Continue with further logic...
            anger_score = emotions['anger']
            disgust_score = emotions['disgust']
            fear_score = emotions['fear']
            joy_score = emotions['joy']
            sadness_score = emotions['sadness']
            
            # Finding the dominant emotion
            emotion_scores = {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score
            }
            dominant_emotion = max(emotion_scores, key=emotion_scores.get)
            
            # Returning the formatted output
            return {
                'anger': anger_score,
                'disgust': disgust_score,
                'fear': fear_score,
                'joy': joy_score,
                'sadness': sadness_score,
                'dominant_emotion': dominant_emotion
            }
        except KeyError as e:
            print(f"KeyError: {e} not found in the response.")
            return formatted_response  # Return the whole response for further inspection
    else:
        # Handle the error in case of an unsuccessful response
        return {"error": f"Request failed with status code {response.status_code}"}

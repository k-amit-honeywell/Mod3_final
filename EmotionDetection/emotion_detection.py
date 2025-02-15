import requests
import json

def emotion_predictor(text_to_analyse):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyse }, "document_emotion": True}

    # Custom header specifying the model ID for the emotion detector service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the emotion analysis API
    response = requests.post(url, json=myobj, headers=header)

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting emotion from the response
    emotions = formatted_response['emotionPredictions'][0]['emotion']

    max_emotion = 0
    max_emotion_dict = {}

    for emotion in emotions:
        if (emotions[emotion] > max_emotion):
            max_emotion = emotions[emotion]
            max_emotion_dict = emotion

        print (emotion, ":", emotions[emotion])
    print ('dominant_emotion', ":", max_emotion_dict)    
    
    # Returning a dictionary containing emotion analysis results
    return {'emotion': max_emotion_dict, 'score' : max_emotion}
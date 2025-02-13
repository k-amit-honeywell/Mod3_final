from EmotionDetection.emotion_detection import emotion_predictor
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection (self):
        # Test case for joy
        result_1 = emotion_predictor('I am glad this happened')
        self.assertEqual(result_1['emotion'], 'joy')
        
        # Test case for anger
        result_2 = emotion_predictor('I am really mad about this')
        self.assertEqual(result_2['emotion'], 'anger')

        # Test case for disgust
        result_3 = emotion_predictor('I feel disgusted just hearing about this')
        self.assertEqual(result_3['emotion'], 'disgust')

        # Test case for sadness
        result_4 = emotion_predictor('I am so sad about this')
        self.assertEqual(result_4['emotion'], 'sadness')

        # Test case for fear
        result_5 = emotion_predictor('I am really afraid that this will happen')
        self.assertEqual(result_5['emotion'], 'fear')

unittest.main()

import requests
import json
api_key = "AIzaSyBKidZ-x86Peckt4EVC5GadfOZpsFMjjcs"
class ImageAnalyzer:
    def __init__(self):
        pass

    def analyze_image(self, https_url):
        """
        Analyzes an image using Google Cloud Vision API and returns the response.
        """
        vision_api_url = "https://vision.googleapis.com/v1/images:annotate"
        payload = {
            "requests": [
                {
                    "image": {
                        "source": {
                            "imageUri": https_url
                        }
                    },
                    "features": [
                        {"type": "LABEL_DETECTION"},
                        {"type": "TEXT_DETECTION"},
                        {"type": "FACE_DETECTION"},
                        {"type": "LANDMARK_DETECTION"}
                    ]
                }
            ]
        }
        response = requests.post(
            vision_api_url,
            params={"key": self.api_key},
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )
        return response.json()

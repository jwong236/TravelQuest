import requests
import json
api_key = "AIzaSyBKidZ-x86Peckt4EVC5GadfOZpsFMjjcs"
class ImageAnalyzer:
    def __init__(self):
        pass

    def identify_objects(self, https_url):
        """
        Analyzes an image using Google Cloud Vision API and returns a list of labels.
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
                        {"type": "LABEL_DETECTION"}
                    ]
                }
            ]
        }
        response = requests.post(
            vision_api_url,
            params={"key": api_key},
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )

        labels = []
        result = response.json()
        if result.get("responses"):
            label_annotations = result["responses"][0].get("labelAnnotations", [])
            labels = [label["description"] for label in label_annotations]

        return labels
    def is_landmark(self, https_url):
        """
        Detects if there is a landmark in an image using Google Cloud Vision API.
        Returns True if a landmark is detected, False otherwise.
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
                        {"type": "LANDMARK_DETECTION"}
                    ]
                }
            ]
        }
        response = requests.post(
            vision_api_url,
            params={"key": api_key},
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )

        result = response.json()
        if result.get("responses"):
            landmark_annotations = result["responses"][0].get("landmarkAnnotations", [])
            return len(landmark_annotations) > 0

        return False
    def detect_emotion(self, https_url):
        """
        Detects emotions on faces in an image using Google Cloud Vision API.
        Returns a dictionary with face number as keys and detected emotions as values.
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
                        {"type": "FACE_DETECTION"}
                    ]
                }
            ]
        }
        response = requests.post(
            vision_api_url,
            params={"key": api_key},
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload)
        )

        emotions = {}
        result = response.json()
        if result.get("responses"):
            face_annotations = result["responses"][0].get("faceAnnotations", [])
            for i, face in enumerate(face_annotations):
                detected_emotions = {
                    "joy": face.get("joyLikelihood"),
                    "sorrow": face.get("sorrowLikelihood"),
                    "anger": face.get("angerLikelihood"),
                    "surprise": face.get("surpriseLikelihood")
                }
                emotions[f"face_{i+1}"] = detected_emotions

        return emotions


if __name__ == "__main__":
    i = ImageAnalyzer()
    print(i.identify_objects("https://traveltriviachallenge.com/wp-content/uploads/2022/10/Sydney-Opera-House-Australia.jpg"))
    print(i.is_landmark("https://californiaunpublished.com/wp-content/uploads/2023/12/venti-views-2td44mctvmI-unsplash-1024x576.jpg"))
    print(i.detect_emotion("https://thumbs.dreamstime.com/b/happy-girl-blue-sky-17121618.jpg"))
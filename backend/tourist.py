import requests
import json

api_key = "AIzaSyBKidZ-x86Peckt4EVC5GadfOZpsFMjjcs"
class TouristClass:
    def __init__(self):
        self.longitude = 0
        self.latitude = 0
    def fetch_current_location(self):
        """
        Uses Google Maps API to retrieve current user coordinates, stored in self.longitude and self.latitude.
        """
        params = {
            'key': api_key
        }
        response = requests.post("https://www.googleapis.com/geolocation/v1/geolocate", params=params).json()
        self.latitude = response["location"]["lat"]
        self.longitude = response["location"]["lng"]
    def get_photo_url(self, photo_reference):
        """
        Converts a photo reference into an HTTPS URL.
        """
        base_url = "https://maps.googleapis.com/maps/api/place/photo"
        params = {
            'maxwidth': 400,
            'photoreference': photo_reference,
            'key': api_key
        }
        response = requests.get(base_url, params=params)
        return response.url

    def get_nearby_poi(self, radius=5000, poi_type='tourist_attraction'):
        """
        Returns a list of locations nearby tourist's current coordinates
        """
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        params = {
            'location': f'{self.latitude},{self.longitude}',
            'radius': radius,
            'type': poi_type,
            'key': api_key
        }
        response = requests.get(url, params=params).json()
        
        pois = []
        if response.get("results"):
            for place in response["results"]:
                p = {
                    "name": place["name"],
                    "photo": self.get_photo_url(place["photos"][0]["photo_reference"]) if "photos" in place and place["photos"] else None,
                    "price_level": place.get("price_level"),
                    "rating": place.get("rating"),
                    "latitude": place["geometry"]["location"]["lat"],
                    "longitude": place["geometry"]["location"]["lng"]
                }
                pois.append(p)

        return pois
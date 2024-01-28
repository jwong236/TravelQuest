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
    def get_nearby_poi(self, radius=5000, limit = 100, poi_type='tourist_attraction'):
        """
        Returns a list of locations nearby tourist's current coordinates
        """
        url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
        params = {
            'location': f'{self.latitude},{self.longitude}',
            'radius': radius,
            'types': poi_type,
            'key': api_key
        }
        response = requests.get(url, params=params).json()
        
        poi_names = []
        if response.get("results"):
            for place in response["results"]:
                p = {
                    "name": place["name"],
                    "photo_reference": place["photos"][0]["photo_reference"] if "photos" in place and place["photos"] else None,
                    "price_level": place.get("price_level"),
                    "rating": place.get("rating"),
                    "latitude": place["geometry"]["location"]["lat"],
                    "longitude": place["geometry"]["location"]["lng"]
                }
                poi_names.append(p)

        return poi_names
"""This module will handle communication between purbeurre application and
google maps API
"""
import os
from .CONSTANTS import STOPWORDS, ACCENTS, QUESTIONS
from .parser import Parser
import requests

class GAPICommunicant():
    """Main class, definig objects that will be able to communicate with 
    google maps API
    """
    
    def __init__(self, parser):
        self.address_str = parser.phrase
        self.payload = None
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json?'
        self.apikey = os.environ['GAPIKEY']
        self.response = None

    def send_requests_for_geocoding(self):
        self.payload = {
            'key': self.apikey,
            'address': self.address_str
        }
        response = requests.get(self.url, self.payload)
        response_json = response.json()
        return response_json['results'][0]['geometry']['location']

if __name__ == '__main__':
    parser = Parser("1600 Amphitheatre Parkway, Mountain View, CA",
        STOPWORDS,
        ACCENTS,
        QUESTIONS
    )
    parser.clean()
    communicant = GAPICommunicant(parser)
    print(communicant.send_requests_for_geocoding())
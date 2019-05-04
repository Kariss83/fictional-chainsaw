"""This module is designed to host all the unit tests for the part of the
program in charge of communication with google API
"""
import os
import json

from app.CONSTANTS import STOPWORDS, ACCENTS, QUESTIONS
from app.gapi import GAPICommunicant
from app.parser import Parser



class MockGet():
    """This class is designed to mock a response object from the module
    requests.
    """
    def __init__(self):
        self.ok = True
        self.response = {
            "results" : [{
                "geometry" : {
                    "location" : {
                        "lat" : 37.4224764,
                        "lng" : -122.0842499
                        }
                    }
                }],
            "status" : "OK"
            }
    
    def json(self):
        return self.response


class TestGAPICommunicant():
    """Main class testing the communication with Google API is fully functional
    """

    def test_requests_response(self, monkeypatch):
        parser = Parser("1600 Amphitheatre Parkway, Mountain View, CA",
            STOPWORDS,
            ACCENTS,
            QUESTIONS
        )
        communicant = GAPICommunicant(parser)
        def mock_requests_get_method(*args):
            mockget = MockGet()
            return mockget
        monkeypatch.setattr('requests.get', mock_requests_get_method)
        result = communicant.make_requests_to_geocoding_API()
        assert result != None 
    
    def test_if_communicant_can_get_gps_coordinates(self, monkeypatch):
        parser = Parser("1600 Amphitheatre Parkway, Mountain View, CA",
            STOPWORDS,
            ACCENTS,
            QUESTIONS
        )
        communicant = GAPICommunicant(parser)
        def mock_requests_get_method(*args):
            mockget = MockGet()
            return mockget
        monkeypatch.setattr('requests.get', mock_requests_get_method)
        communicant.make_requests_to_geocoding_API()
        result = communicant.get_data_from_geocoding()
        assert result == {
                    "lat": 37.4224764,
                    "lng": -122.0842499
                    }


if __name__ == '__main__':
    print(os.environ['GAPIKEY'])

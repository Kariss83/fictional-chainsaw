"""This module is designed to host all the unit tests for the part of the
program in charge of communication with google API
"""
import os
import json

from app.CONSTANTS import STOPWORDS, ACCENTS, QUESTIONS
from app.gapi import GAPICommunicant
from app.parser import Parser


class TestGAPICommunicant():
    """Main class testing the communication with Google API is fully functional
    """

    def test_requests_response_when_ok(self, monkeypatch):
        
        class MockGet():
            """This class is designed to mock a response object from the module
            requests.
            """
            def __init__(self, *args):
                self.ok = True
            
        parser = Parser("1600 Amphitheatre Parkway, Mountain View, CA",
            STOPWORDS,
            ACCENTS,
            QUESTIONS
        )
        communicant = GAPICommunicant(parser)
        monkeypatch.setattr('requests.get', MockGet)
        result = communicant.make_requests_to_geocoding_API()
        assert result != None 
    
    def test_if_communicant_can_get_gps_coordinates(self, monkeypatch):
        
        class MockGet():
            """This class is designed to mock a response object from the module
            requests.
            """
            def __init__(self, *args):
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

        parser = Parser("1600 Amphitheatre Parkway, Mountain View, CA",
            STOPWORDS,
            ACCENTS,
            QUESTIONS
        )
        communicant = GAPICommunicant(parser)
        monkeypatch.setattr(communicant,'response', MockGet())
        result = communicant.get_data_from_geocoding()
        assert result == {
                    "lat": 37.4224764,
                    "lng": -122.0842499
                    }


if __name__ == '__main__':
    print(os.environ['GAPIKEY'])

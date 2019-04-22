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

    def test_if_communicant_can_get_gps_coordinates(self):
        parser = Parser("1600 Amphitheatre Parkway, Mountain View, CA",
            STOPWORDS,
            ACCENTS,
            QUESTIONS
        )
        communicant = GAPICommunicant(parser)
        result = communicant.send_requests_for_geocoding()
        assert result == {
                    "lat": 37.4253904,
                    "lng": -122.0844873
                    }


if __name__ == '__main__':
    print(os.environ['GAPIKEY'])

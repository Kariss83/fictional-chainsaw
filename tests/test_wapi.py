"""This module is designed to host all the unit tests for the part of the
program in charge of communication with google API
"""

from app.CONSTANTS import STOPWORDS, ACCENTS, QUESTIONS
from app.gapi import GAPICommunicant
from app.wapi import WAPICommunicant
from app.parser import Parser

class MockGetGeo():
    """This class is designed to mock a response object from the module
    requests.
    """
    def __init__(self):
        self.ok = True
        self.response = {
            "query": {
				"geosearch":[{
					"pageid":736,
					"ns":0,
					"title":"Academy of Art University",
					"lat":37.78785,
					"lon":-122.40065,
					"dist":129.9,
					"primary":""
				}]
			}
		}
    
    def json(self):
        return self.response

class MockGetPages():
    """This class is designed to mock a response object from the module
    requests.
    """
    def __init__(self):
        self.ok = True
        self.response = {
            "query":{
				"pages":{
					"736":{
						"pageid":736,
						"title":"Albert Einstein",
						"extract":"""Albert Einstein ( EYEN-styne; German:
						[ˈalbɛɐ̯t ˈʔaɪnʃtaɪn] (listen); 14 March 1879 – 18
						April 1955) was a German-born theoretical physicist
						who developed the theory of relativity, one of the
						two pillars of modern physics (alongside quantum
						mechanics). His work is also known for its influence
						on the philosophy of science. He is best known to the
						general public for his mass–energy equivalence formula
						E = mc2, which has been dubbed \"the world's most
						famous equation\"."""
					}
				}
			}
		}
    
    def json(self):
        return self.response

class Tests_WAPIcommunicant():
	"""This class will contain all tests that concern the communication
	with wikimedia API
	"""

	def test_communicant_can_get_answer_from_the_API(self, monkeypatch):
		"""Docstring
		"""
		parser = Parser("1600 Amphitheatre Parkway, Mountain View, CA",
			STOPWORDS,
			ACCENTS,
			QUESTIONS
		)
		gcommunicant = GAPICommunicant(parser)
		gcommunicant.make_requests_to_geocoding_API()
		def mock_requests_get_method(*args):
			mockget = MockGetGeo()
			return mockget
		monkeypatch.setattr('requests.get', mock_requests_get_method)
		wcommunicant = WAPICommunicant(gcommunicant)
		result = wcommunicant.make_requests_to_wikigeo_api()
		assert result != None

	def test_communicant_can_get_pageid_of_POI(self, monkeypatch):
		"""Docstring
		"""
		parser = Parser("1600 Amphitheatre Parkway, Mountain View, CA",
			STOPWORDS,
			ACCENTS,
			QUESTIONS
		)
		gcommunicant = GAPICommunicant(parser)
		gcommunicant.make_requests_to_geocoding_API()
		def mock_requests_get_method(*args):
			mockget = MockGetGeo()
			return mockget
		monkeypatch.setattr('requests.get', mock_requests_get_method)
		wcommunicant = WAPICommunicant(gcommunicant)
		wcommunicant.make_requests_to_wikigeo_api()
		result = wcommunicant.get_pageid_of_close_point_of_interest()
		assert result == 736

	def test_communicant_can_get_info_from_page(self, monkeypatch):
		"""Docstring
		"""
		parser = Parser("1600 Amphitheatre Parkway, Mountain View, CA",
			STOPWORDS,
			ACCENTS,
			QUESTIONS
		)
		gcommunicant = GAPICommunicant(parser)
		gcommunicant.make_requests_to_geocoding_API()
		def mock_requests_getgeo_method(*args):
			mockget = MockGetGeo()
			return mockget
		monkeypatch.setattr('requests.get', mock_requests_getgeo_method)
		wcommunicant = WAPICommunicant(gcommunicant)
		wcommunicant.make_requests_to_wikigeo_api()
		def mock_requests_get_method(*args):
			mockget = MockGetPages()
			return mockget
		monkeypatch.setattr('requests.get', mock_requests_get_method)
		wcommunicant.get_pageid_of_close_point_of_interest()
		result = wcommunicant.get_data_from_page()
		assert result == """Albert Einstein ( EYEN-styne; German:
						[ˈalbɛɐ̯t ˈʔaɪnʃtaɪn] (listen); 14 March 1879 – 18
						April 1955) was a German-born theoretical physicist
						who developed the theory of relativity, one of the
						two pillars of modern physics (alongside quantum
						mechanics). His work is also known for its influence
						on the philosophy of science. He is best known to the
						general public for his mass–energy equivalence formula
						E = mc2, which has been dubbed \"the world's most
						famous equation\"."""
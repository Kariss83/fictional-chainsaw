"""This module is designed to host all the unit tests for the part of the
program in charge of communication with google API
"""

from app.CONSTANTS import STOPWORDS, ACCENTS, QUESTIONS
from app.gapi import GAPICommunicant
from app.wapi import WAPICommunicant
from app.parser import Parser


class Tests_WAPIcommunicant():
	"""This class will contain all tests that concern the communication
	with wikimedia API
	"""

	def test_communicant_can_get_answer_from_the_API(self):
		"""Docstring
		"""
		class MockGCommunicant():
			def get_data_from_geocoding(self):
				return {"lat" : 37.4224764, "lng" : -122.0842499}
		wcommunicant = WAPICommunicant(MockGCommunicant())
		result = wcommunicant.make_requests_to_wikigeo_api()
		assert result != None

	def test_communicant_can_get_pageid_of_POI(self, monkeypatch):
		"""Docstring
		"""
		PAGE_ID = 736
		class MockResponse:
			def json(self):
				return {
					'query': {
						'geosearch': [{
							'pageid': PAGE_ID
						}]
					}
				}
		monkeypatch.setattr(WAPICommunicant, '__init__', lambda self: None)
		obj = WAPICommunicant()
		obj.response = MockResponse()
		assert obj.get_pageid_of_close_point_of_interest() == PAGE_ID
	
	def test_communicant_can_get_info_from_page(self, monkeypatch):
		"""Docstring
		"""
		def MockInit(self):
			self._url = 'https://en.wikipedia.org/w/api.php?'
			self.pageid = 736
			
		class MockResponse():
			def __init__(self, *args):
				pass
			def json(self):
				data = {
				"query":{
					"pages":{
						"736":{
							"extract":"""Albert Einstein ( EYEN-styne; German:
							[ˈalbɛɐ̯t ˈʔaɪnʃtaɪn] (listen); 14 March 1879 – 18
							April 1955) was a German-born theoretical physicist
							who developed the theory of relativity, one of the
							two pillars of modern physics (alongside quantum
							mechanics). His work is also known for its
							influence on the philosophy of science. He is best
							known to the general public for his mass–energy
							equivalence formula E = mc2, which has been dubbed
							\"the world's most famous equation\"."""
							}
						}
					}
				}
				return data
		monkeypatch.setattr(WAPICommunicant, '__init__', MockInit)
		monkeypatch.setattr('app.wapi.requests.get', MockResponse)
		wcommunicant = WAPICommunicant()
		result = wcommunicant.get_data_from_page()
		assert result =="""Albert Einstein ( EYEN-styne; German:
							[ˈalbɛɐ̯t ˈʔaɪnʃtaɪn] (listen); 14 March 1879 – 18
							April 1955) was a German-born theoretical physicist
							who developed the theory of relativity, one of the
							two pillars of modern physics (alongside quantum
							mechanics). His work is also known for its
							influence on the philosophy of science. He is best
							known to the general public for his mass–energy
							equivalence formula E = mc2, which has been dubbed
							\"the world's most famous equation\"."""

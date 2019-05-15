"""This module will handle communication between purbeurre application and
wikimedia API
"""
import os
from .CONSTANTS import STOPWORDS, ACCENTS, QUESTIONS
from .parser import Parser
from .gapi import GAPICommunicant
import requests

class WAPICommunicant():
	"""This class is designed to make communication with wikimedia API.
	"""
	def __init__(self, gcommunicant):
		self._coord_raw = gcommunicant.get_data_from_geocoding()
		self._lat = str(self._coord_raw['lat'])
		self._lng = str(self._coord_raw['lng'])
		self._coords = f"{self._lat}|{self._lng}"
		self._url = 'https://en.wikipedia.org/w/api.php?'
		self.response = None
		self.pageid = None

	def make_requests_to_wikigeo_api(self):
		"""This method is used to make the HTML request.
		"""
		payload = {
			'action': 'query',
			'format': 'json',
			'gscoord': self._coords,
			'gsradius': 10000,
			'list': 'geosearch'
		}
		self.response = requests.get(self._url, payload)
		if self.response.ok:
			return True
		else:
			return None
	
	def get_pageid_of_close_point_of_interest(self):
		"""This method will retrieve page id of a point of interest
		close to the coordinates.
		"""
		response_json = self.response.json()
		self.pageid = response_json['query']['geosearch'][0]['pageid']
		return self.pageid

	def get_data_from_page(self):
		payload = {
			'action': 'query',
			'format': 'json',
			'pageids': self.pageid,
			'prop': 'extracts',
			'explaintext': True,
			'exintro': True
		}
		response_page = requests.get(self._url, payload)
		response_page_json = response_page.json()['query']['pages']
		return response_page_json[str(self.pageid)]['extract']
		

if __name__ == "__main__":
	parser = Parser("1600 Amphitheatre Parkway, Mountain View, CA",
				STOPWORDS,
				ACCENTS,
				QUESTIONS
			)
	gcommunicant = GAPICommunicant(parser)
	gcommunicant.make_requests_to_geocoding_API()
	wcommunicant = WAPICommunicant(gcommunicant)
	result = wcommunicant.get_pageid_of_close_point_of_interest()
	print(result)
	

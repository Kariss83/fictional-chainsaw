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
		self.coord_raw = gcommunicant.get_data_from_geocoding()
		self.lat = str(self.coord_raw['lat'])
		self.lng = str(self.coord_raw['lng'])
		self.coords = f"{self.lat}|{self.lng}"
		self.url = 'https://en.wikipedia.org/w/api.php?'
		self.payload = None
		self.response = None
		self.response_json = None
		self.response_page = None
		self.response_page_json = None
		self.pageid = None

	def make_requests_to_wikigeo_api(self):
		"""This method is used to make the HTML request.
		"""
		self.payload = {
			'action': 'query',
			'format': 'json',
			'gscoord': self.coords,
			'gsradius': 10000,
			'list': 'geosearch'
		}
		self.response = requests.get(self.url, self.payload)
		if self.response.ok:
			return True
		else:
			return None
	
	def get_pageid_of_close_point_of_interest(self):
		"""This method will retrieve page id of a point of interest
		close to the coordinates.
		"""
		self.response_json = self.response.json()
		self.pageid = self.response_json['query']['geosearch'][0]['pageid']
		return self.response_json['query']['geosearch'][0]['pageid']

	def get_data_from_page(self):
		self.payload = {
			'action': 'query',
			'format': 'json',
			'pageids': self.pageid,
			'prop': 'extract'
		}
		self.response_page = requests.get(self.url, self.payload)
		self.response_page_json = self.response_page.json()['query']['pages']
		return self.response_page_json[str(self.pageid)]['extract']
		

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
	

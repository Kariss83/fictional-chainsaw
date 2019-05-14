"""This module is running the full backend and send it to flask"""

from app import parser, gapi, wapi


def main():
	phrase = input("Qu'avez vous à dire à GranpyBot?")
	parser = parser.Parser(phrase)
	parser.clean()
	gcommunicant = gapi.GAPICommunicant(parser)
	gcommunicant.make_requests_to_geocoding_API()
	gcommunicant.get_data_from_geocoding()
	wcommunicant = wapi.WAPICommunicant(gcommunicant)
	wcommunicant.make_requests_to_wikigeo_api()
	wcommunicant.get_pageid_of_close_point_of_interest()
	wcommunicant.get_data_from_page()
	json_return = {
		'return' : wcommunicant.get_data_from_page
	}

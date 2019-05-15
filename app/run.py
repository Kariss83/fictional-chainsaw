from .parser import Parser
from .gapi import GAPICommunicant
from .wapi import WAPICommunicant
from .CONSTANTS import STOPWORDS, ACCENTS, QUESTIONS

import json

if __name__ == '__main__':
    answer = input("What would you like to tell to GrandPy today?")
    parser = Parser(answer, STOPWORDS, ACCENTS, QUESTIONS)
    parser.phrase = parser.clean()
    gcommunicant = GAPICommunicant(parser)
    gcommunicant.make_requests_to_geocoding_API()
    wcommunicant = WAPICommunicant(gcommunicant)
    wcommunicant.make_requests_to_wikigeo_api()
    wcommunicant.get_pageid_of_close_point_of_interest()
    infos = wcommunicant.get_data_from_page()
    dict_return = {'data': infos}
    json_return = json.dumps(dict_return)
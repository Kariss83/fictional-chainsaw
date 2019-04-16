from app.parser import Parser
from app.CONSTANTS import *


class TestParserPurBeurre():

    def test_parser_can_clean_spaces(self):
        parser = Parser()
        result = parser.clear_spaces("   Bonjour tout le monde")
        assert result == "Bonjourtoutlemonde"

    def test_parser_can_morph_into_a_list(self):
        parser = Parser()
        result = parser.morph_into_a_list("Bonjour tout le monde")
        assert result == ["Bonjour", "tout", "le", "monde"]

    def test_parser_can_remove_stop_words(self):
        parser = Parser()
        result = parser.remove_stop_words(STOPWORDS,
            "Allo allo a Brignoles Paris")
        assert result == ["brignoles", "paris"]

# module utiliser par google appelé googlemaps avec un pipenv.
# py media wiki
# requests sur mediawiki, se servir de la doc pour trouver les exemples

from app.parser import Parser
from app.CONSTANTS import STOPWORDS, PONCTUATION, ACCENTS, QUESTIONS


class TestParserPurBeurre():

    def test_parser_can_remove_accents(self):
        parser = Parser(
            "bienvenue à lès brignoles",
            STOPWORDS,
            ACCENTS,
            QUESTIONS
        )
        result = parser.remove_accents()
        assert result == "bienvenue a les brignoles"

    def test_parser_can_remove_stop_words(self):
        parser = Parser(
            "la tour eiffel",
            STOPWORDS,
            ACCENTS,
            QUESTIONS
        )
        result = parser.remove_stop_words()
        assert result == "tour eiffel"

    def test_parser_can_retrieve_info_after_some_words(self):
        parser = Parser(
            "Bonjour Grandpy, peux-tu me dire l'adresse de la tour Eiffel?",
            STOPWORDS,
            ACCENTS,
            QUESTIONS
        )
        result = parser.get_end_of_question()
        assert result == "la tour Eiffel"

    def test_parser_can_return_clean_of_all_output(self):
        parser = Parser(
            "Bonjour Grandpy, peux-tu me dire l'adresse de la tour Eiffèl?",
            STOPWORDS,
            ACCENTS,
            QUESTIONS
        )
        result = parser.clean()
        assert result == "tour eiffel"

# module utiliser par google appelé googlemaps avec un pipenv.
# py media wiki
# requests sur mediawiki, se servir de la doc pour trouver les exemples

import re

from .CONSTANTS import STOPWORDS, ACCENTS, QUESTIONS


class Parser():
    """This class is designed to transform the user input into a readable
    request that we will be able to send to the google API
    """

    def __init__(self, phrase, stopwords, accents, question_bloc):
        self.phrase = phrase
        self.stopwords = stopwords
        self.accents = accents
        self.questions = question_bloc

    def remove_stop_words(self):
        word_list = self.phrase.lower().split(" ")
        for word in self.stopwords:
            while word in word_list:
                word_list.remove(word)
        phrase_str = ' '.join(word_list)
        return phrase_str

    def remove_accents(self):
        for key in self.accents:
            self.phrase = self.phrase.replace(key, self.accents[key])
        return self.phrase

    def get_end_of_question(self):
        for block in self.questions:
            match = re.search(r"l'adresse de (?P<lieu>[^,;.:?!]*)[,;.:?!]?.*$",
                              self.phrase
                             )
        if match != None:
            self.phrase = str(match.group('lieu'))
        return self.phrase

    def clean(self):
        """Launch all the other methods to clean the input"""
        self.phrase = self.phrase.lower()
        self.phrase = self.remove_accents()
        self.get_end_of_question()
        return self.remove_stop_words()


if __name__ == '__main__':
    user_input = str(input())
    parser = Parser("bonjour", STOPWORDS, ACCENTS, QUESTIONS)
    print(parser.remove_stop_words(STOPWORDS, user_input))

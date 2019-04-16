from .CONSTANTS import STOPWORDS


class Parser():
    """This class is designed to transform the user input into a readable
    request that we will be able to send to the google API
    """
    def __init__(self, phrase, stopwords):
        self.phrase = phrase
        self.stopwords = stopwords

    def clear_spaces(self, phrase):
        return phrase.replace(" ", "")

    def morph_into_a_list(self, phrase):
        return phrase.split(" ")

    def remove_stop_words(self, stop_list, phrase):
        word_list = phrase.lower().split(" ")
        for word in stop_list:
            while word in word_list:
                word_list.remove(word)
        return word_list
        # rajouter un join pour revenir sur une chaine de caractère.
    def clean(self):
        """Launch all the other methods to clean the input"""

if __name__ == '__main__':
    user_input = str(input())
    parser = Parser()
    print(parser.remove_stop_words(STOPWORDS, user_input))

# spliter après l'expression qui introduit la question de lieu.

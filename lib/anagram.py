# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, list_of_words):
        def split_word(word):
            return sorted([letter for letter in word])
        return [word for word in list_of_words if split_word(word) == split_word(self.word)]
    pass

from random_words import get_words_from_file
class Anagram_checker():
    def __init__(self):
        self.words = get_words_from_file()

    def valid_word(self,word):
          if word in self.words:
            print("{} word exists".format(word))
          else:
            print('no word found')
            return

    def get_anagrams(self,word1):
        anagram = []
        for word in (self.words):
            if sorted(word) == sorted(word1):
                anagram.append(word)
        return anagram



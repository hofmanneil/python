import AnangramCheck,random_words
from AnangramCheck import Anagram_checker



while True:
    print("""++++++Anagrams Menu+++++++++
    1-Enter your word 
    2-Exit""" )
    choice = input('Please enter a number  ')
    if choice == "1":
        word = input("Please enter a word ")
        check = Anagram_checker()
        check.valid_word(word)
        anagrams = check.get_anagrams(word)
        print(anagrams)
    else:
        print('No input found ')
    if choice == "2" :
        break




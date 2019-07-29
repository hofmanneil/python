import random,os
def get_words_from_file():
    if os.path.exists("wordproject"):
        f = open("wordproject", "r")
        words =[]
        for line in f:
            words.append(line.strip().lower())
        return words
def get_random_words(lenth):
        words = get_words_from_file()
        random_words = random.choices(words, k=lenth)
        for word in random_words:
            word = word.lower()
def get_random_sentance(lenth):
    words=get_words_from_file()
    random_words = random.choices(words, k=lenth)
    sentance = " "
    for word in random_words:
        sentance += word+' '
# second way
#sentance =' '.join(random_words)











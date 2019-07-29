import random
from random_words import get_words_from_file

def get_sentance():
    sentance = input("Please type a sentance ")
    print(sentance)
    return sentance

def mask_sentance():
    sentance1 = get_sentance()
    sentance = sentance1.split()
    random_words = random.choices(get_words_from_file(),k=len(sentance))
    masked = []
    for e in range(len(sentance)):
        masked.append(sentance[e])
        masked.append(random_words[e])
    return masked

def unmask_sentance():
    mask = mask_sentance()


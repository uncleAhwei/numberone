#! python2
import time

pyg = 'ay'



while True:
    original = raw_input('Enter a word:')
    if len(original) > 0 and original.isalpha():
        word = original.lower()
        first = word[0]
        new_word = word[1:] + first + pyg
        print new_word
    continue


    if original.lower() == "quit" or original.lower() == "done": break





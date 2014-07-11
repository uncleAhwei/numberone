pyg = "ay"
original = raw_input("Enter a word to translate it into pig latin:")
if len(original) > 0 and original.isalpha():
    word = original.lower()
    first = word[0]
    new_word = word[1:] + first + pyg
    print new_word
    continue
else:
    print "You didn't type a word, dummy! Words only have letters, no numbers or spaces, please."
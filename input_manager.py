import string


# infer words from user input
def tokenize(user_input):
    sentence = user_input.lower()
    words = sentence.split()
    # remove punctuation
    for word in words:
        for elem in word:
            if elem in string.punctuation:
                word_no_pun = word.replace(elem, "")
                words.remove(word)
                words.append(word_no_pun)  # note: words are no longer in order


# return the most important key for the words given as input
def find_key(words):
    print("heaviest key")
    # find if there are keys and choose the one with the highest value
    # keys and sentences: dictionary structure
    # TODO: search the word in key synset, order key, take the heaviest key

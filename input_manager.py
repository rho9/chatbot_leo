import string
import keys_manager as km


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
    km.find_answer(words)

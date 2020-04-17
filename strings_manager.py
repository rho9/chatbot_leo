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
    return words


def replace_a_star(sentence, replacement):
    return sentence.replace("*", replacement)


def complete_keywords(sentence, keyword):
    # soft implementation: it simply takes the string next to the keyword until it finds a dot
    to_add = (sentence.split(keyword)[1]).split(".")[0]
    modified = keyword + to_add
    return modified

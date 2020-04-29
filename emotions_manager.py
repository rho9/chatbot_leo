from data import knowledge_base as knm

# used to create emotions files
def to_lower(start_file, final_file):
    start = open(start_file, "r")
    final = open(final_file, "a")
    for line in start:
        final.write(line.lower())
    start.close()
    final.close()


# used to create emotions files
def to_alphabetical_order(start_file, final_file):
    start = open(start_file, "r")
    final = open(final_file, "a")
    pos_list = []
    for line in start:
        pos_list.append(line)
    pos_list.sort()
    final.write("\n[negative]\n")
    for word in pos_list:
        final.write(word)
    start.close()
    final.close()


# it counts positive and negative emotions
# Frequency? after every session? after each sentence?
def emo_counter(words):
    pos_counter = 0
    neg_counter = 0
    print(words)
    for word in words:
        if word in knm.pos_emos:
            pos_counter += 1
        elif word in knm.neg_emos:
            neg_counter += 1
    return pos_counter, neg_counter

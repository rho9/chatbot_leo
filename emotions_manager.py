def to_lower(start_file, final_file):
    start = open(start_file, "r")
    final = open(final_file, "a")
    for line in start:
        final.write(line.lower())
    start.close()
    final.close()

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
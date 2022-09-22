punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(w):
    for l in w:
        if l in punctuation_chars:
            w = w.replace(l, "")
    return w



positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())

def get_pos(line):
    pos = 0
    words = line.split(" ")
    for w in words:
        if strip_punctuation(w).lower() in positive_words:
            pos += 1
    return pos


print(get_pos("BORDER Terrier puppy. Name is loving and very protective of the people she loves. Name2 is a 3 year old Maltipoo. Name3 is an 8 year old Corgi."))
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(w):
    for l in w:
        if l in punctuation_chars:
            w = w.replace(l, "")
    return w



negative_words = []
with open("negative_words.txt") as neg_f:
    for lin in neg_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def get_neg(line):
    neg = 0
    words = line.split(" ")
    for w in words:
        if strip_punctuation(w).lower() in negative_words:
            neg += 1
    return neg


print(get_neg("BORDER Terrier puppy. Name is loving and very protective of the people she loves. Name2 is a 3 year old Maltipoo. Name3 is an 8 year old Corgi."))
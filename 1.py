punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(w):
    for l in w:
        if l in punctuation_chars:
            w = w.replace(l, "")
    return w

print(strip_punctuation("@Py!t,ho n.k"))
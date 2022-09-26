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



input_file = "project_twitter_data.csv"
output_file = "resulting_data.csv"

# import csv 
def dictReader(file):
    result = []
    keys = file.readline().strip().split(',')
    for l in file:
        values = l.strip().split(',')
        temp_dict = dict(zip(keys, values))
        result.append(temp_dict)
    return result

def dictWrite(file, keys, data):
    header = ','.join(keys) + "\n"
    file.write(header)
    for d in data:
        line = ','.join([str(d[k]) for k in keys]) + '\n'
        file.write(line)


input_datas = []
with open(input_file, 'r') as f:
    reader = dictReader(f)
    for x in reader:
        input_datas.append(x)

for t in input_datas:
    t["pos_count"] = get_pos(t["tweet_text"])
    t["neg_count"] = get_neg(t["tweet_text"])
    t["net_score"] = get_pos(t["tweet_text"]) - get_neg(t["tweet_text"])


# from pprint import pprint
# pprint(input_datas)

with open(output_file, 'w') as f:
    dictWrite(f, ['tweet_text', 'retweet_count', 'reply_count', 'pos_count', 'neg_count', 'net_score'], input_datas)
    # writer.writeheader()
    # writer.writerows(input_datas)

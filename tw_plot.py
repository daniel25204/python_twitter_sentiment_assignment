import csv 

input_datas = []
with open("resulting_data.csv", 'r') as f:
    reader = csv.DictReader(f)
    for x in reader:
        input_datas.append(x)


import matplotlib.pyplot as plt
# print(sorted([int(x["net_score"]) for x in input_datas]))
# print(sorted([int(x["retweet_count"]) for x in input_datas]))
result_tup = []
for x in input_datas:
    result_tup.append((x["net_score"], x["retweet_count"]))
print(result_tup)

plt.scatter([int(x[0]) for x in result_tup], [int(x[1]) for x in result_tup], s=30, c='lightseagreen')
plt.title('Number of Retweets vs Net Score', fontsize=15)		
plt.xlabel('Net Score', fontsize=10)		
plt.ylabel('Number of Retweets', fontsize=10)
plt.show()
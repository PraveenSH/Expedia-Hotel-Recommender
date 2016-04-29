print('importing libraries...')
from csv import DictReader
from collections import defaultdict

print('defining functions...')
def get_top5(d):
    return " ".join(sorted(d, key=d.get, reverse=True)[:5])

destination_clusters = defaultdict(lambda: defaultdict(int))

print('applying simple clustering...')
for i, row in enumerate(DictReader(open("../input/train.csv"))):
	destination_clusters[(row["srch_destination_id"],row["srch_destination_type_id"])][row["hotel_cluster"]] += int(row["cnt"])
	
most_frequent = defaultdict(str)

print('finding most popular local hotels...')
for k in destination_clusters:
	most_frequent[k] = get_top5(destination_clusters[k])

print('creating submission...')
with open("pred_sub.csv", "w") as outfile:
	outfile.write("id,hotel_cluster\n")
	for i, row in enumerate(DictReader(open("../input/test.csv"))):
		outfile.write("%d,%s\n"%(i, most_frequent[(row["srch_destination_id"],row["srch_destination_type_id"])]))
print('finsihed.')

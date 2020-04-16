# Big Data_Quiz 4_Question 1.2
from pyspark import SparkContext
sc = SparkContext()

from operator import add

rx = sc.textFile("gs://example0211/chicago-taxi-rides.csv")

def compute_contribs(neighbors, rank):
    sum_traffic = 0
    for ngr in neighbors:
        sum_traffic += ngr[1]
    for ngr in neighbors:
        rank_new = rank*ngr[1]/sum_traffic
        yield (ngr[0], rank_new)

# remove the head of RDD
clean_rx = rx.filter(lambda x: x.split(',')[0].isdigit())

# create a map of pickup & dropoff & traffic for each trip
trips = clean_rx.map(lambda x: (int(x.split(',')[0]), (int(x.split(',')[1]), int(x.split(',')[2]))))

# create a pair RDD (area, [(neighbor_area, neighbor_traffic)])
links = trips.groupByKey().distinct().mapValues(lambda x: list(x)).cache()

# Start each area at a rank of 1 [(14, 1), (29, 1), (41, 1), ...]
ranks = trips.map(lambda x : (x[0], 1)).distinct()


for i in range(50):
    contribs = links.join(ranks).flatMap(lambda x: compute_contribs(x[1][0], x[1][1]))
    ranks = contribs.reduceByKey(add).mapValues(lambda rank : rank * 0.85 + 0.15)

for (link, rank) in ranks.collect():
    print("%s has rank %s." % (link, rank))
    
ranks.saveAsTextFile("gs://example0211/output")

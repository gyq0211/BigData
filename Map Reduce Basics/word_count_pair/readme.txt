Instead of the built-in aggregate function used on slide 12 of Hadoop on GCP (Links to an external site.), write your own reducer and run wordcount on the books in the five-books collection in Canvas. Hint: it may be useful to first test your mapper and reducer with a single small file without a cluster by using

mapper.py < small_text_file.txt | reducer.py > small_count.txt
Obtain a Hadoop cluster with 1 master and 2 slaves, similar to the suggested configuration on slide 11 but with 2 slave devices and obtain word counts for the books in five-books.

Region	us-central1 (or another region in the US)
Master node	Single Node (1 master, 2 workers)
Machine type	n1-standard-4 (4 vCPU, 15.0 GB memory)
Primary disk type	pd-standard
Primary disk size	2000 GB

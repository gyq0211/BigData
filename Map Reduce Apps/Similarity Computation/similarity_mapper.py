#!/usr/bin/env python

import sys
import os
import string
from itertools import combinations

all_president_list = os.environ['all_presidents'].split(",")

all_president_pairs = list(combinations(all_president_list, 2))


for line in sys.stdin:
    line = line.rstrip('\n')
    word, president_set = line.split("\t")
    president_set = eval(president_set)

    for president_pair in all_president_pairs:
        exits_in_any = 0
        exits_in_two = 0
        if president_pair[0] in president_set or president_pair[1] in president_set:
            exits_in_any = 1
        if president_pair[0] in president_set and president_pair[1] in president_set:
            exits_in_two = 1
        print("%s\t%s" % (president_pair, [exits_in_any, exits_in_two]))
    

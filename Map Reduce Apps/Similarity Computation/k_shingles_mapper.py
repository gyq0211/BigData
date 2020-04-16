#!/usr/bin/env python

import os
import sys
import string

n = int(os.environ['window'])
shingle_type = os.environ['shingle_type']

filepath = os.environ["mapreduce_map_input_file"]
president = filepath.split("/")[-1].split('_')[0]

for line in sys.stdin:
    for i in line:
        if i in string.punctuation:
            line = line.replace(i, " ")
    line = line.lower()
    line = line.strip()

    if shingle_type == 'word':
        line = line.split()

    for i in range(len(line) - n + 1):
        print("%s\t%s" % (line[i: i+n], president))

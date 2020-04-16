#!/usr/bin/env python

import sys, re
import string
from collections import defaultdict

window = 2


for line in sys.stdin:
    for i in line:
        if i in string.punctuation:
            line = line.replace(i, " ")
    line = line.lower()
    line = line.strip()
    twits = line.split()
    i = 0
    word_cnt = defaultdict(dict)
    for i in range(len(twits) - 1):
        word_cnt[twits[i]][twits[i + 1]] = word_cnt[twits[i]].get(twits[i + 1], 0) + 1
    for word, cnt in word_cnt.items():
        print("%s\t%s" % (word, dict(cnt)))

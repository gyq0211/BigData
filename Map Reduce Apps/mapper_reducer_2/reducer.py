#!/usr/bin/env python

from operator import itemgetter
import sys
import string
from collections import Counter

a = None
b = Counter()
cur_word = None

for line in sys.stdin:
    line = line.strip()
    cur_word, cnt = line.split('\t')
    cnt = Counter(eval(cnt))

    if a == cur_word:
        b += cnt
    else:
        if a:
            total_cnt = sum(b.values())
            for k, v in sorted(b.items()):
                print('%s|%s\t%.4f' % (a, k, v * 1.0 / total_cnt))
        b = cnt
        a = cur_word

if a == cur_word:
    total_cnt = sum(b.values())
    for k, v in sorted(b.items()):
        print('%s|%s\t%.4f' % (a, k, v * 1.0 / total_cnt))

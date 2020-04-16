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
            for k, v in sorted(b.items()):
                print('%s|%s\t%s' % (a, k, v))
        b = cnt
        a = cur_word

if a == cur_word:
    for k, v in sorted(b.items()):
        print('%s|%s\t%s' % (a, k, v))

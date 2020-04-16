#!/usr/bin/env python
import sys

word = None
president_set = set()

for line in sys.stdin:
    line = line.rstrip('\n')
    cur_word, president = line.split('\t')

    if word == cur_word:
        president_set.add(president)
    else:
        if word:
            print('%s\t%s' % (word, president_set))
        president_set = {president}
        word = cur_word
        
if word != None:
    print('%s\t%s' % (word, president_set))

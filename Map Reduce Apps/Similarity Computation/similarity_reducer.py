#!/usr/bin/env python
import sys

president_pair = None
similarity_cnt = [0, 0]

for line in sys.stdin:
    line = line.rstrip('\n')
    cur_president_pair, cur_similarity_cnt = line.split('\t')
    cur_president_pair = eval(cur_president_pair)
    cur_similarity_cnt = eval(cur_similarity_cnt)

    if cur_president_pair == president_pair:
        similarity_cnt[0] += cur_similarity_cnt[0]
        similarity_cnt[1] += cur_similarity_cnt[1]
    else:
        if similarity_cnt and similarity_cnt[0] != 0:
            print('%s\t union:%d, intersection:%d, similarity:%.4f' % (president_pair, similarity_cnt[0], similarity_cnt[1], similarity_cnt[1] * 1.0 / similarity_cnt[0]))
        president_pair = cur_president_pair
        similarity_cnt = cur_similarity_cnt
        
if president_pair != None and similarity_cnt[0] != 0:
    print('%s union:%d, intersection:%d, similarity:%.4f' % (president_pair, similarity_cnt[0], similarity_cnt[1], 1.0 * similarity_cnt[1] / similarity_cnt[0]))

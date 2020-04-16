#!/usr/bin/env python
import sys

current_book = None
current_word = None
current_count = 0
word = None

for line in sys.stdin:

    line = line.strip()
    book, word, count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:

        continue

    if current_book == book & current_word == word:
        current_count += count
    else:
        if current_word:
            print '%s\t%s' % (current_book, current_word, current_count)
        current_count = count
        current_word = word
        current_book = book
if current_word == word:
    print '%s\t%s' % (current_book, current_word, current_count)
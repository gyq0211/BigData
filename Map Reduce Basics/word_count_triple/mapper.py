#!/usr/bin/env python
import sys
# input comes from STDIN (standard input)

for line in sys.stdin:

    books = book.split()

    line = line.strip()

    words = line.split()

    for book in books:
        for word in words:

            print '%s\t%s' % (book, word, 1)
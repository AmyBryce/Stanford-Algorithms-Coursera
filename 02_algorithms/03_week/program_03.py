#! /usr/bin/env python

import sys

from heapq import heappush, heappop

f = open(sys.argv[1])

heaplow = []
heaphigh = []
cumulative_median = 0

for line in f.readlines():
    # Extract the number from the line in the file.
    number = int(line[:-1])

    # Special case when heaplow is empty (i.e. the first time through the loop).
    if len(heaplow) == 0:
        heappush(heaplow, -number)
        cumulative_median += -heaplow[0]
        continue

    # Always negate `number` before inserting into `heaplow`
    # so that we can extract the 'max' rather than the 'min' key from it.
    maxlow = -heaplow[0]

    if number <= maxlow:
        heappush(heaplow, -number)
    else:
        heappush(heaphigh, number)

    if len(heaphigh) > len(heaplow):
        heappush(heaplow, -heappop(heaphigh))
    elif len(heaplow) > len(heaphigh) + 1:
        heappush(heaphigh, -heappop(heaplow))

    cumulative_median += -heaplow[0]

print (cumulative_median % 10000)

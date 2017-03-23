#! /usr/bin/env python

import sys

f = open(sys.argv[1])

values = set([int(line[:-1]) for line in f.readlines()])
targets = range(-10000, 10000)
num_found = 0

for t in targets:
    for x in values:
        y = t - x

        if x != y and y in values:
            num_found += 1
            break

print num_found

#! /usr/bin/env python

import sys

f = open(sys.argv[1])

visited = []
num_targets = 0

# Build an array of values from each line in the file.
# values = []
# for line in f.readlines():
# values.append(int(line[:-1]))
values = [int(line[:-1]) for line in f.readlines()]

for v1 in values:
    visited.append((v1, v1))

    for v2 in values:
        if v1 < v2:
           pair = (v1, v2)
        elif v2 < v1:
           pair = (v2, v1)
        else:
           pair = (v2, v2)

        if pair in visited:
            continue

        sum = pair[0] + pair[1]
        if sum >= -10000 and sum <= 10000:
            num_targets += 1

        visited.append(pair)

print num_targets

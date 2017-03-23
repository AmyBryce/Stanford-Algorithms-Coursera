# Your task is to code up and run the randomized contraction algorithm for the min cut problem
# and use it on the above graph to compute the min cut.
import copy
import math
import re
import random
import sys

# adjacency list -> dictionary
a = {}

f = file("kargerMinCut.txt")

for line in f.readlines():
    # remove trailing whitespace
    line = line.rstrip()

    # split by tabs -> list of strings
    line = re.split(r'\t+', line)

    # make first element the key, then rest is the value
    a[line[0]] = line[1:]

def mincut(b):
    while True:
        if len(b.keys()) == 2:
            # print cut
            return len(b[b.keys()[0]])

        # pick random edge
        node1 = random.choice(b.keys())
        node2 = random.choice(b[node1])

        # contract edge
        list1 = b[node1]
        list2 = b[node2]

        superlist = list1 + list2

        # remove self-loop
        superlist = filter(lambda node: not (node == node1 or node == node2), superlist)

        # delete node from dictionary
        del b[node1]
        del b[node2]

        # created the supernode
        b[node1] = superlist

        for node in b.keys():
            for i in range(len(b[node])):
                if b[node][i] == node2:
                    b[node][i] = node1

numberofcalls = len(a) * len(a) * math.log(len(a))
minvalue = sys.maxint
for i in range(int(100)):
    value = mincut(copy.deepcopy(a))
    if value < minvalue:
        minvalue = value
    if i % 1000 == 0:
        print i

print minvalue

# ans 17

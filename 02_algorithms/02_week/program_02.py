import sys
import re

def splitColumn(column):
    node, distance = column.split(',')
    return [node, int(distance)]

def buildNodes(fileName):
    f = file(fileName)
    nodes = {}

    for line in f.readlines():
        # remove trailing whitespace
        line = line.rstrip()
        # split by tabs -> list of strings
        line = re.split(r'\t+', line)

        nodes[line[0]] = map(splitColumn, line[1:])

    return nodes

def dijkstra(unvisited, visited):
    while True:
        for vertex in unvisited:
            if vertex in visited:
                return visited
            visited.update(vertex)
            print vertex


    return visited

if __name__ == "__main__":
    filename = sys.argv[1]

    unvisited = buildNodes(filename)
    visited = {}
    shortestPaths = {}

    print unvisited

    print dijkstra(unvisited, visited)

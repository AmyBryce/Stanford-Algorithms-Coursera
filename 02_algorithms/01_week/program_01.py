# Your task is to code up the algorithm from the video lectures for
# computing strongly connected components (SCCs),
# and to run this algorithm on the given graph.
# You should output the sizes of the 5 largest SCCs in the given graph,
# in decreasing order of sizes, separated by commas (avoid any spaces).

import collections
import sys

class Node(object):
    def __init__(self, label):
        self.label = label
        self.children = []

    def addChild(self, node):
        self.children.append(node)

    def __str__(self):
        string = "Node: {label}\n".format(label=self.label)
        for child in self.children:
            string += "  --> {child}\n".format(child=child.label)
        return string

def buildRevNodes(fileName):
    f = file(fileName)
    nodes = {}

    for line in f.readlines():
        # remove trailing whitespace
        line = line.rstrip()
        # split by spaces -> [list] of strings
        line = line.split()

        nodes.setdefault(line[0], Node(line[0]))
        nodes.setdefault(line[1], Node(line[1]))

        nodes[line[1]].addChild(nodes[line[0]])

    return nodes

def buildNodes(fileName):
    f = file(fileName)
    nodes = {}

    for line in f.readlines():
        # remove trailing whitespace
        line = line.rstrip()
        # split by spaces -> [list] of strings
        line = line.split()

        nodes.setdefault(line[0], Node(line[0]))
        nodes.setdefault(line[1], Node(line[1]))

        nodes[line[0]].addChild(nodes[line[1]])

    return nodes

def dfs_recursive(node, S, visited):
    if visited[node.label]:
        return

    visited[node.label] = True

    # base cases:
    if not node.children: # empty lists are 'falsy'
        # add node to stack
        S.appendleft(node)
        return

    for child in node.children:
        if not visited[child.label]:
            dfs(child, S, visited)

    S.appendleft(node)

def dfs_iterative(node, visited, callback):
    stack = collections.deque()
    stack.appendleft(node)

    while stack:
        node = stack.popleft()
        visited[node.label] += 1

        if visited[node.label] == 1:
            stack.appendleft(node)

            for child in node.children:
                if not visited[child.label]:
                    stack.appendleft(child)

        elif visited[node.label] == 2:
            callback(node)

if __name__ == "__main__":
    filename = sys.argv[1]

    S = collections.deque()
    sccSizes = collections.defaultdict(lambda: 0)

    def pushToS(node):
        S.appendleft(node.label)

    nodesRev = buildRevNodes(filename)
    visited = collections.defaultdict(lambda: 0)
    for node in nodesRev.values():
        if not visited[node.label]:
            dfs_iterative(node, visited, pushToS)

    def incrementSccSize(label):
        sccSizes[label] += 1

    nodes = buildNodes(filename)
    visited = collections.defaultdict(lambda: False)
    for label in S:
        if not visited[label]:
            dfs_iterative(nodes[label], visited, lambda node: incrementSccSize(label))

    sortedSccSizes = sorted(sccSizes.items(), key=lambda item: item[1], reverse=True)

    print sortedSccSizes[:5]

# ('287144', 434821), ('609317', 968), ('328524', 459), ('33604', 313), ('389700', 211)

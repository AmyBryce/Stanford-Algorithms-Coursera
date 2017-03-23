import sys
import re

def buildNodes(fileName):
    f = file(fileName)
    nodes = {}

    for line in f.readlines():
        # remove trailing whitespace
        line = line.rstrip()
        # split by tabs -> list of strings
        line = re.split(r'\t+', line)

        distances = {}
        for column in line[1:]:
            node, distance = column.split(',')
            distances[node] = int(distance)

        nodes[line[0]] = distances

    return nodes

if __name__ == "__main__":
    filename = sys.argv[1]

    distances = buildNodes(filename)
    nodes = distances.keys()
    answers = []


    ####################################################
    # UPDATE TO USE THE METHOD SUGGESTED IN THE LECTURES
    ####################################################
    # unvisited = {node: None for node in nodes} #using None as +inf
    # visited = {}
    # current = '1'
    # currentDistance = 0
    # unvisited[current] = currentDistance

    # while True:
    #     for neighbour, distance in distances[current].items():
    #         if neighbour not in unvisited:
    #             continue

    #         newDistance = currentDistance + distance

    #         if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
    #             unvisited[neighbour] = newDistance

    #     visited[current] = currentDistance
    #     del unvisited[current]

    #     if not unvisited:
    #         break

    #     candidates = [node for node in unvisited.items() if node[1]]
    #     current, currentDistance = sorted(candidates, key = lambda x: x[1])[0]

        # we want the distances for 7,37,59,82,99,115,133,165,188,197
        if current == '7' or current == '37' or current == '59' or current == '82' or current == '99' or current == '115' or current == '133' or current == '165' or current == '188' or current == '197':
        # if current == '7' or current == '4' or current == '1' or current == '82':
            answers.append((int(current), currentDistance))


    # {'115': 2399, '59': 2947, '197': 3068, '37': 2610, '133': 2029, '99': 2367, '7': 2599, '82': 2052, '165': 2442, '188': 2505}
    # [(7, 2599), (37, 2610), (59, 2947), (82, 2052), (99, 2367), (115, 2399), (133, 2029), (165, 2442), (188, 2505), (197, 3068)]


    sortedAnswers = sorted(answers, key=lambda x: x[0])
    cleanAnswers = map(lambda x: x[1], sortedAnswers)

    print sortedAnswers
    print cleanAnswers
    # print visited

    # ANS 2599,2610,2947,2052,2367,2399,2029,2442,2505,3068


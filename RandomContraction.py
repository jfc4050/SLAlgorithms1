import random
import sys


class Graph:
    def __init__(self):
        self.graph = {}

    def add(self, node, edges):
        self.graph[node] = edges


def readGraph(filename, graph):
    file = open(filename)
    for line in file:
        node = int(line.split()[0])
        edges = []
        for edge in line.split()[1:]:
            edges.append(int(edge))
        graph.add(node, edges)


def contraction(myGraph, node1, node2):
    for node3 in myGraph.graph[node2]:              # for each node that node2 is connected to:
        if node3 != node1:                          # if node is not node1 (so no self loops):
            (myGraph.graph[node1]).append(node3)    # node1 absorbs node3
            (myGraph.graph[node3]).append(node1)
        myGraph.graph[node3].remove(node2)          # remove node2 from node3

    del myGraph.graph[node2]                        # finally, delete node 2


def minCuts(myGraph):
    minCut = sys.maxsize
    for node in list(myGraph.graph.keys()):
        cuts = len(list(myGraph.graph[node]))
        if cuts < minCut:
            minCut = cuts
    return "minCuts: " + str(minCut)


def randomizeContraction(myGraph):
    while len(myGraph.graph) > 2:
        # pick random node from myGraph
        randNode1 = random.choice(list(myGraph.graph.keys()))
        # pick random node2 (that is connected to node1)
        randNode2 = random.choice(myGraph.graph[randNode1])
        contraction(myGraph, randNode1, randNode2)
    return minCuts(myGraph)


def main():
    # filename = ""

    myGraph = Graph()
    myGraph.add(1, [2, 4])
    myGraph.add(2, [1, 3, 4])
    myGraph.add(3, [2, 4])
    myGraph.add(4, [1, 2, 3])
    print("graph: ", myGraph.graph)

    # readGraph(filename, myGraph)
    print(randomizeContraction(myGraph))

main()
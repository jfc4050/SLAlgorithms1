import random
import sys


class Graph:
    def __init__(self):
        self.graph = {}

    def addNode(self, node, edges):
        self.graph[node] = edges


def readGraph(filename, graph):
    file = open(filename)
    for line in file:
        arr = line.split()
        node = int(arr[0])
        edges = [int(x) for x in arr[1:]]
        graph.addNode(node, edges)


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
    return minCut


def randomizeContraction(myGraph):
    while len(myGraph.graph) > 2:
        randNode1 = random.choice(list(myGraph.graph.keys()))      # pick random node from myGraph
        randNode2 = random.choice(myGraph.graph[randNode1])        # pick random node2 (that is connected to node1)
        contraction(myGraph, randNode1, randNode2)
    return minCuts(myGraph)


def main():
    filename = "/Users/justin/Documents/Documents/Projects/PyCharm Projects/SLAlgorithms1/txt files/kargerMinCut.txt"

    minimum = sys.maxsize
    for i in range(200):
        myGraph = Graph()
        readGraph(filename, myGraph)
        currentAns = randomizeContraction(myGraph)
        print(currentAns)
        if currentAns < minimum:
            minimum = currentAns
        del myGraph
    print("minimum is ", minimum)


main()

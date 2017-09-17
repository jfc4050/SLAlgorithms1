class Queue:
    def __init__(self, initValue=None):
        self.items = [initValue]

    def empty(self):
        return self.items == []

    def enqueue(self, itemIn):
        self.items.insert(0, itemIn)

    def dequeue(self):
        return self.items.pop()

    def print(self):
        print(self.items)


def breadthFirstSearch(graph, query, start='A', testing=True):
    explored = set(start)
    que = Queue(graph[start])

    if start == query:
        return 0

    dist = 1
    while not que.empty():
        edges = que.dequeue()
        for node in edges:
            if node not in explored:
                explored.add(node)

                if testing:
                    assert len(explored) <= len(graph)

                if node == query:
                    return dist
                elif que.empty():
                    dist += 1

                que.enqueue(graph[node])


def main():
    graph = {'A': {'B', 'C'},
             'B': {'A', 'D', 'E'},
             'C': {'A', 'F'},
             'D': {'B'},
             'E': {'B', 'F'},
             'F': {'C', 'E'}}
    query = 'E'
    print(breadthFirstSearch(graph, query))


main()

import json
from timeit import default_timer

# dijkstra's algorithm

graph_file = "test_graph.json"

with open(graph_file, "r") as rf:
    graph_contents = rf.read()

graph = json.loads(graph_contents)
S

def dijkstra_path_finder(graph, start, end):
    startTime = default_timer()

    shortest_distance = {}
    predecessor = {}
    unseenNodes = graph
    infinity = 9999999
    path = []

    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:
        minNode = None
        for node in unseenNodes:
            if minNode is None:
                minNode = node
            elif shortest_distance[node] < shortest_distance[minNode]:
                minNode = node

        for childNode, weight in graph[minNode].items():
            if weight + shortest_distance[minNode] < shortest_distance[childNode]:
                shortest_distance[childNode] = weight + shortest_distance[minNode]
                predecessor[childNode] = minNode

        unseenNodes.pop(minNode)

    currentNode = end
    while currentNode != start:
        try:
            path.insert(0, currentNode)
            currentNode = predecessor[currentNode]
        except KeyError:
            print("Path not reachable")
            break

    path.insert(0, start)

    if shortest_distance[end] != infinity:
        print(f'Shortest Distance is {str(shortest_distance[end])}')
        print(f'And the path is {(path)}')

    endTime = default_timer()
    print(f"RunTime: {endTime-startTime}")


dijkstra_path_finder(graph, "a", "e")

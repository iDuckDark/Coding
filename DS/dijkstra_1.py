from graph_examples import graph_weighted


def dijkstra(graph, start):
    nodes = graph.keys()
    distances = graph
    unvisited = {node: None for node in nodes}  # using None as +inf
    visited = {}
    current = start
    currentDistance = 0
    unvisited[current] = currentDistance
    counter = 1
    while True:
        counter += 1
        for neighbour, distance in distances[current].items():
            if neighbour not in unvisited:
                continue
            newDistance = currentDistance + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited:
            break
        candidates = [_ for _ in unvisited.items() if _[1]]
        current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]
    print(visited)


dijkstra(graph_weighted, 'A')

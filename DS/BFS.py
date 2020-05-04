from graph_examples import graph_1, graph_2

def BFS(graph, start):
    visited, queue, path = set(), [start], []
    while queue:
        current = queue.pop(0)
        if current not in visited:
            visited.add(current)
            path.append(current)
            queue.extend(graph[current])
    return path

print(BFS(graph_1, "0"))

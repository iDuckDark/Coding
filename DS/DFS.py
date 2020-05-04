from graph_examples import graph_1, graph_2


# Option 1
def DFS(graph, start):
    visited, stack, path = set(), [start], []
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.add(current)
            path.append(current)
            stack.extend(graph[current])
    return path


# Option 2
def DFS_paths(graph, start, end):
    stack = [(start, [start])]
    visited = set()
    while stack:
        (vertex, path) = stack.pop()
        if vertex not in visited:
            if vertex == end:
                return path
            visited.add(vertex)
            for neighbor in graph[vertex]:
                stack.append((neighbor, path + [neighbor]))


print(DFS(graph_1, '0'))
print(DFS_paths(graph_2, 'A', 'F'))

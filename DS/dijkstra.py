from graph_examples import graph_weighted
import heapq


def dijkstra(graph, start):
    dist_from_start = {start: 0}
    previous = {}
    heap = [(0, start)]
    while heap:
        current = heapq.heappop(heap)[1]
        print(heap)
        for neighbour, cost in graph[current].items():
            alt_cost = dist_from_start[current] + cost
            if alt_cost < dist_from_start.get(neighbour, float("inf")):
                heapq.heappush(heap, (alt_cost, neighbour))
                dist_from_start[neighbour] = alt_cost
                previous[neighbour] = current
    # print(dist_from_start)
    return previous


def get_path(prev, target):
    path = []
    while target in prev:
        path.insert(0, target)
        target = prev[target]
    return path


previous = dijkstra(graph_weighted, 'A')
# print(get_path(previous, 'C'))

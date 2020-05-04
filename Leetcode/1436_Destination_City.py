
from pprint import pprint


class Solution(object):
    def buildGraph(self, paths):
        graphs = {}
        for path in paths:
            start, end = path[0], path[1]
            if start not in graphs:
                graphs[start] = set([end])
            else:
                graphs[start].add(end)
        return graphs

    def destCity(self, paths):
        graphs = self.buildGraph(paths)
        pprint(graphs)
        print()
        visited = set()
        direction = []
        stack = [paths[0][0]]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                direction.append(current)
                if current not in graphs:
                    return current
                for neighbour in graphs[current]:
                    stack.append(neighbour)
        return direction[-1]


# paths = [["London", "New York"], ["New York", "Lima"], ["Lima", "Sao Paulo"]]
# paths = [["B","C"],["D","B"],["C","A"]]
# paths = [["A","Z"]]


paths = [
    ["jMgaf WaWA", "iinynVdmBz"],
    [" QCrEFBcAw", "wRPRHznLWS"],
    ["iinynVdmBz", "OoLjlLFzjz"],
    ["OoLjlLFzjz", " QCrEFBcAw"],
    ["IhxjNbDeXk", "jMgaf WaWA"],
    ["jmuAYy vgz", "IhxjNbDeXk"]
]

sol = Solution().destCity(paths)
pprint(sol)

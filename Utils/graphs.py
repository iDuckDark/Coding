def buildGraph(self, paths):
    graphs = {}
    for path in paths:
        start, end = path[0], path[1]
        if start not in graphs:
            graphs[start] = set([end])
        else:
            graphs[start].add(end)
    return graphs

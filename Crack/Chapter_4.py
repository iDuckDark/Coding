class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TreeNode:

    def __init__(self):
        self.root = None

    def print(self):
        self.printDFS(self.root)

    def printDFS(self, root):
        if root is not None:
            print(root.value)
            self.printDFS(root.left)
            self.printDFS(root.right)

    def add(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add(self.root, value)

    def _add(self, current, value):
        if current.value < value:
            if current.right is not None:
                self._add(current.right, value)
            else:
                current.right = Node(value)
        else:
            if current.left is not None:
                self._add(current.left, value)
            else:
                current.left = Node(value)

    def getHeight(self, current):
        if current is None:
            return 0
        return max(self.getHeight(current.left), self.getHeight(current.right)) + 1

    def isBalanced(self):
        return self._isBalanced(self.root)

    def _isBalanced(self, current):
        if current is None:
            return True
        heightDifference = abs(self.getHeight(
            current.left) - self.getHeight(current.right))
        if heightDifference > 1:
            return False
        return self._isBalanced(current.left) and self._isBalanced(current.right)


def makeTree():
    # values = [5, 4, 3, 2, 1, 7, 8]
    values = [5, 6, 4]
    treeNode = TreeNode()
    for v in values:
        treeNode.add(v)
    treeNode.print()
    print()
    print(treeNode.isBalanced())


makeTree()


class Graph:

    def __init__(self, graph):
        self.graph = graph
        # print(self.graph)

    def add(self, A, B):
        if A not in self.graph:
            self.graph[A] = set()
        self.graph[A].add(B)

    def printer(self):
        print(self.graph)

    def getNeighbours(self, current):
        neighbours = self.graph[current]

    def DFS(self, start, target):
        stack = [start]
        visited = set()
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.add(current)
                print(current)
                if current == target:
                    break
                for neighbour in self.graph[current]:
                    stack.append(neighbour)

    def BFS(self, start, target):
        queue = [start]
        visited = set()
        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.add(current)
                print(current)
                if current == target:
                    break
                for neighbour in self.graph[current]:
                    queue.append(neighbour)

    def getNeighbor(self, neighbors, graph):
        out = set()
        for neighbor in neighbors:
            out = out.union(graph[neighbor])
        return out

    def tierCount(self, start, target):
        graph = self.graph
        if target in graph[start]:
            return 1
        else:
            visited = set()
            queue = self.getNeighbor(graph[start], graph)
            count = 2
            while queue:
                if target in queue:
                    return count
                else:
                    count += 1
                    visited = visited.union(queue)
                    queue = self.getNeighbor(queue, graph) - visited
        return 0


def runGraph():
    graph = Graph({'0': {'1', '2'},
                   '1': {'0', '3', '4'},
                   '2': {'0'},
                   '3': {'1'},
                   '4': {'2', '3'}})
    print(graph.tierCount('0', '3'))

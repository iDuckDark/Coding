class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


class TreeNode:

    def __init__(self, values=None):
        self.root = None
        if values:
            [self.add(_) for _ in values]

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
        heightDifference = abs(self.getHeight(current.left) - self.getHeight(current.right))
        if heightDifference > 1:
            return False
        return self._isBalanced(current.left) and self._isBalanced(current.right)


def mergeTrees(t1, t2):
    if t1 is None:
        return t2
    if t2 is None:
        return t1
    t1.val += t2.val
    t1.left = mergeTrees(t1.left, t2.left)
    t1.right = mergeTrees(t1.right, t2.right)
    return t1


def makeTree():
    print('TreeNode: ')
    treeNode = TreeNode([5, 6, 4])
    treeNode.print()
    print('Is Balance: ', treeNode.isBalanced())

    # t1 = TreeNode([1, 3, 2, 5])
    # t2 = TreeNode([2, 1, 3, None, 4, None, 7])
    # t3 = mergeTrees(t1, t2)


makeTree()

import unittest

class Node:
    def __init__(self, x, left=None, right=None):
        self.x = x
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root):
        self.root = root

    def Paths(self, node, value):
        if not node:
            return 0
        thisNode = self.GetTheSum(node, value, 0)
        leftSide = self.Paths(node.left, value)
        rightSide = self.Paths(node.right, value)

        return thisNode + leftSide + rightSide

    def PathsWrapper(self, value):
        return self.Paths(self.root, value)

    def GetTheSum(self, node, value, curr):
        if not node:
            return 0
        x = curr + node.x
        output = 0
        if x == value:
            output = 1
        output += self.GetTheSum(node.left, value, x)
        output += self.GetTheSum(node.right, value, x)
        return output


class tests(unittest.TestCase):
    a = Node(3)
    b = Node(-2)
    c = Node(1, a, b)
    d = Node(4)
    e = Node(-2)
    f = Node(-1, d, e)
    g = Node(4, c, f)
    h = Node(-1)
    i = Node(2, h)
    j = Node(3)
    k = Node(-2, j, i)
    root = Node(3, g, k)

    tree = Tree(root)

    data = [
        (5,1),
        (3,7),
        (7,2)
    ]

    def test_working(self):
        for [input, expected] in self.data:
            output = self.tree.PathsWrapper(input)
            self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
    #O(nlgn)
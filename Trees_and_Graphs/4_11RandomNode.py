import random

class Node:
    def __init__(self, x, left=None, right=None, p=None):
        self.x = x
        self.left = left
        self.right = right
        self.p = p
        self.size = 0

class Tree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, x):
        newNode = Node(x)
        itera = self.root
        y = None
        while itera:
            y = itera
            if newNode.x < itera.x:
                itera = itera.left
            else:
                itera = itera.right

        if not y:
            self.root = newNode
        elif newNode.x < y.x:
            y.left = newNode
        else:
            y.right = newNode
        newNode.p = y

        while newNode:
            newNode.size += 1
            newNode = newNode.p

    def pickRandom(self):
        if not self.root:
            return False
        i = random.randint(1, self.root.size)
        return self.findRandom(i, self.root)

    def findRandom(self, i, node):
        r = 1
        if node.left:
            r = node.left.size + 1
        if i == r:
            return node
        elif i < r:
            return self.findRandom(i, node.left)
        else:
            return self.findRandom(i-r, node.right)


if __name__ == '__main__':
    tree = Tree()
    tree.insert(5)
    tree.insert(1)
    tree.insert(4)
    tree.insert(4)
    tree.insert(5)
    tree.insert(9)
    tree.insert(7)
    tree.insert(13)
    tree.insert(3)
    print(tree.pickRandom().x)
    print(tree.pickRandom().x)
    print(tree.pickRandom().x)


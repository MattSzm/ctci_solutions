import unittest

class Node:
    def __init__(self, node):
        self.Tnode = node
        self.next = None

class LinkedList:
    def __init__(self, node=None):
        if not node:
            self.head = None
        else:
            self.head = Node(node)

    def insert(self, node):
        if not node:
            return
        k = Node(node)
        k.next = self.head
        self.head = k

    def __iter__(self):
        it = self.head
        while it:
            yield it.Tnode
            it = it.next

    def isempty(self):
        if not self.head:
            return True
        return False

class TreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right

class Tree:
    def __init__(self, rootNode):
        self.root = rootNode

def ListOfDepths(tree):
    LinkedLists = []
    this_lvl = LinkedList(tree.root)
    while not this_lvl.isempty():
        LinkedLists.append(this_lvl)
        next_lvl = LinkedList()
        for single in this_lvl:
            if single:
                next_lvl.insert(single.left)
                next_lvl.insert(single.right)
        this_lvl = next_lvl
    return LinkedLists


if '__main__' == __name__:
    A = TreeNode(8)
    B = TreeNode(7, right=A)
    C = TreeNode(5)
    D = TreeNode(2, left=B, right=C)
    E = TreeNode(3)
    F = TreeNode(5)
    G = TreeNode(6, left=E, right=F)
    root = TreeNode(3, left=D, right=G)
    tree = Tree(root)

    linkedLists = ListOfDepths(tree)

    for single in linkedLists:
        for i in single:
            print(i.value)
        print('\n')


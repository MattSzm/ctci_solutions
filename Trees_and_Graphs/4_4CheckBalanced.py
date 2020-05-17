import unittest

class Node:
    def __init__(self, left=None, right=None, x=None):
        self.key = x
        self.left = left
        self.right = right

class Tree:
    def __init__(self, root=None):
        self.root = root
        self.Redflag = False

    def CheckBalance(self, x):
        if x.left:
            leftDepth = self.CheckBalance(x.left) + 1
        else:
            leftDepth = 0
        if x.right:
            rightDepth =self.CheckBalance(x.right) + 1
        else:
            rightDepth = 0

        if rightDepth-leftDepth>1 or leftDepth-rightDepth>1:
            self.Redflag = True
        return max(rightDepth, leftDepth)

    def CheckBalanceMaintain(self):
        if self.root:
            TreeDepth = self.CheckBalance(self.root)
        else:
            return False, 0

        if self.Redflag:
            return False, TreeDepth
        return True, TreeDepth

class tests(unittest.TestCase):
    A1=Node()
    B1=Node(left=A1)
    C1=Node()
    D1=Node()
    E1=Node(left=C1,right=D1)
    F1=Node(left=B1,right=E1)
    G1=Node()
    H1=Node(right=G1)
    I1=Node()
    J1=Node(left=I1,right=H1)
    Root1=Node(left=F1,right=J1)

    tree = Tree(Root1)

    A2 = Node()
    B2 = Node(left=A1)
    C2 = Node()
    D2 = Node(left=B2,right=C2)
    E2 = Node()
    F2 = Node()
    G2 = Node(left=E2, right=F2)
    H2 = Node(right=G2)
    Root2 = Node(left=D2, right=H2)

    tree2 = Tree(Root2)

    tree3 = Tree()

    def test_True(self):
        result, depth = self.tree.CheckBalanceMaintain()
        self.assertTrue(result)
        self.assertEqual(depth, 3)

    def test_False(self):
        result, depth = self.tree2.CheckBalanceMaintain()
        self.assertFalse(result)
        self.assertEqual(depth, 3)

        result, depth = self.tree3.CheckBalanceMaintain()
        self.assertFalse(result)
        self.assertEqual(depth, 0)

if __name__ == '__main__':
    unittest.main()
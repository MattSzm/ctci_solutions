import unittest

class Node:
    def __init__(self, x, left=None, right=None):
        self.x=x
        self.left=left
        self.right=right


def search(t1, t2)->bool:
    if not t1:
        return False
    if checkSubree(t1, t2):
        return True

    left = search(t1.left, t2)
    right = search(t1.right, t2)
    return left or right

def checkSubree(t1, t2):
    if not t1 and not t2:
        return True
    elif not t1 or not t2:
        return False
    elif t1.x != t2.x:
        return False

    left = checkSubree(t1.left, t2.left)
    right = checkSubree(t1.right, t2.right)
    return left and right

class tests(unittest.TestCase):
    a = Node(1)
    b = Node(4)
    c = Node(3,a,b)
    d = Node(9,c)
    e = Node(5)
    f = Node(12)
    g = Node(15, e, f)
    root = Node(4,d,g)

    a1 = Node(1)
    b1 = Node(4)
    c1 = Node(3, a1, b1)

    def test_true(self):
        output = search(self.root, self.c1)
        self.assertTrue(output)


if __name__ == '__main__':
    unittest.main()
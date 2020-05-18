import unittest

class Node:
    def __init__(self, x, left=None, right=None, p=None):
        self.left = left
        self.right = right
        self.p = p
        self.x = x

def Successor(x):
    if not x:
        return False
    if x.right:
        x=x.right
        while x.left:
            x=x.left
        return x
    elif not x.p:
        return False
    elif x.p.right and x.p.right == x:
        while x.p and x.p.right==x:
            x=x.p
    if x.p:
        return x.p
    return False


class tests(unittest.TestCase):
    a = Node(1)
    b = Node(3)
    c = Node(2, a, b)
    a.p = c
    b.p = c
    d = Node(5)
    e = Node(7)
    f = Node(6, d, e)
    d.p = f
    e.p = f
    g = Node(4, c, f)
    c.p = g
    f.p = g
    z = Node(9)
    h = Node(10, left=z,right=None)
    z.p = h
    i = Node(15)
    j = Node(20)
    k = Node(17, left=i, right=j)
    i.p = k
    j.p = k
    l = Node(13, left=h, right=k)
    h.p = l
    k.p = l
    root = Node(8, g, l)
    g.p = root
    l.p = root

    dataT = [
        (root,9),
        (l,15),
        (k,20),
        (i,17),
        (a,2),
        (z,10),
        (f,7),
        (e,8),
        (g,5)
    ]
    dataF = [j]

    def test_working(self):
        for [input,expected] in self.dataT:
            output = Successor(input)
            self.assertEqual(output.x, expected)

    def test_false(self):
        output = Successor(self.dataF[0])
        self.assertFalse(output)

if __name__ == '__main__':
    unittest.main()

import unittest

class Node:
    def __init__(self, key):
        self.k = key
        self.adj = []
        self.s = False

class Graph:
    def __init__(self, vertices):
        self.V = vertices

    def BFS(self, f, s):
        if f == s:
            return True
        for item in self.V:
            item.s = False
        f.s = True
        queue = [f]
        while queue:
            item = queue.pop(0)
            for adj in item.adj:
                if not adj.s:
                    if adj == s:
                        return True
                    else:
                        adj.s = True
                        queue.append(adj)
        return False

class Test(unittest.TestCase):
    A = Node(1)
    B = Node(2)
    C = Node(3)
    D = Node(4)
    E = Node(5)
    A.adj = [E]
    B.adj = [A,C,D]
    D.adj = [B]
    E.adj = [C]
    graph = Graph([A,B,C,D,E])

    dataT = (
        (D,E),
        (B,C),
        (A,A)
    )
    dataF = (
        (E,D),
        (A,B)
    )

    def test(self):
        for test in self.dataT:
            result = self.graph.BFS(*test)
            self.assertTrue(result)
        for test in self.dataF:
            result = self.graph.BFS(*test)
            self.assertFalse(result)

if '__main__' == __name__:
    unittest.main()
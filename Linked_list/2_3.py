import unittest

class Node:
    def __init__(self, data, next=None):
        self.data=data
        self.next=next

class LinkedList:
    def __init__(self):
        self.head = None

def delete_middle_node(x):
    if not x or not x.next:
        return False
    next = x.next
    x.data = next.data
    x.next = next.next
    return True

class tests(unittest.TestCase):
    F = Node('f')
    E = Node('e', F)
    D = Node('d', E)
    C = Node('c', D)
    B = Node('b', C)
    A = Node('a', B)
    linkedList = LinkedList()
    linkedList.head = A

    def delete_middle_node_test(self):
         output = delete_middle_node(self.C)
         self.assertTrue(output)
         output = delete_middle_node(self.F)
         self.assertFalse(output)

if '__main__' == __name__:
    unittest.main()
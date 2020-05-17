import unittest

class Node:
    def __init__(self,x,next=None):
        self.x=x
        self.next=next

class LinkedList:
    def __init__(self, head=None):
        self.head=head

def Palindrome(linkedList):
    if not linkedList.head:
        return False
    slow = linkedList.head
    fast = linkedList.head
    stack = []
    while fast and fast.next:
        stack.append(slow)
        slow=slow.next
        fast=fast.next.next

    if fast:
        slow = slow.next

    while slow:
        if slow.x != stack.pop().x:
            return False
        slow=slow.next

    return True

def Palindrome2(linkedList):
    if not linkedList.head:
        return False
    reversedList, size = ReverseLinked(linkedList)
    itera = linkedList.head
    reversedItera = reversedList.head
    for i in range(int(size/2)):
        if itera.x != reversedItera.x:
            return False
        itera = itera.next
        reversedItera = reversedItera.next
    return True

def ReverseLinked(linkedList):
    head = None
    itera = linkedList.head
    size = 0
    while itera != None:
        new_Node = Node(itera.x)
        new_Node.next = head
        head = new_Node
        itera = itera.next
        size += 1
    return LinkedList(head), size


class tests(unittest.TestCase):
    a = Node('A')
    b = Node('B', a)
    c = Node('C', b)
    d = Node('B', c)
    e = Node('A', d)
    linked = LinkedList(e)

    a1 = Node('A')
    b1 = Node('E', a1)
    c1 = Node('C', b1)
    d1 = Node('B', c1)
    e1 = Node('A', d1)
    linked2 = LinkedList(e1)

    def test_True(self):
        output = Palindrome(self.linked)
        self.assertTrue(output)
        output = Palindrome2(self.linked)
        self.assertTrue(output)

    def test_False(self):
        output = Palindrome(self.linked2)
        self.assertFalse(output)
        output = Palindrome2(self.linked2)
        self.assertFalse(output)
        output = Palindrome2(LinkedList())
        self.assertFalse(output)


if __name__ == '__main__':
    unittest.main()
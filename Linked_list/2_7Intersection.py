import unittest

class Node:
    def __init__(self, x, next=None):
        self.x=x
        self.next=next

class Linkedlist:
    def __init__(self, head=None):
        self.head=head

def IntersectionFalseOrTrue(linkedListOne, linkedListTwo)->bool:
    memory = linkedListOne.head
    reversedLinkedListOne = ReverseInPlace(linkedListOne)

    iter=linkedListTwo.head
    while iter.next:
        iter=iter.next
    if memory == iter:
        return True
    return False


def ReverseInPlace(linkedList):
    head = None
    memory = linkedList.head
    while memory:
        iter = memory
        memory = memory.next
        iter.next = head
        head = iter
    return head

def Intersection(linkedListOne, linkedListTwo):
    lenghtOne = 1
    lenghtTwo = 1

    iteraOne=linkedListOne.head
    while iteraOne.next:
        lenghtOne += 1
        iteraOne = iteraOne.next

    iteraTwo=linkedListTwo.head
    while iteraTwo.next:
        lenghtTwo += 1
        iteraTwo = iteraTwo.next

    if iteraOne != iteraTwo:
        return False

    if lenghtOne>lenghtTwo:
        longer=linkedListOne
        shorter=linkedListTwo
    else:
        longer=linkedListTwo
        shorter=linkedListOne

    iteraLonger = longer.head
    for i in range(abs(lenghtTwo-lenghtOne)):
        iteraLonger = iteraLonger.next

    iteraShorter = shorter.head
    while iteraLonger != iteraShorter:
        iteraLonger = iteraLonger.next
        iteraShorter = iteraShorter.next

    return iteraShorter

class tests(unittest.TestCase):
    g = Node('g')
    f = Node('f', g)
    e = Node('e', f)
    d = Node('d', e)
    c = Node('c', d)
    b = Node('b', f)
    a = Node('a', b)

    h = Node('h')
    i = Node('i', h)
    j = Node('j', i)

    linkedListOne = Linkedlist(a)
    linkedListTwo = Linkedlist(c)
    linkedListThree = Linkedlist(j)

    def test_working(self):
        output = Intersection(self.linkedListOne, self.linkedListTwo)
        self.assertEqual(output, self.f)

    def test_False(self):
        output = Intersection(self.linkedListOne,self.linkedListThree)
        self.assertFalse(output)


if __name__ == '__main__':
    unittest.main()

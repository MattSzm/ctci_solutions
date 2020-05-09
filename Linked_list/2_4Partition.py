class Node:
    def __init__(self, key, next=None):
        self.k = key
        self.next = next

class LinkedList:
    def __init__(self, headNode):
        self.head = headNode

    def lenght(self):
        iter = self.head
        count = 1
        while iter.next:
            count += 1
            iter = iter.next
        return count

    def returnLast(self):
        iter = self.head
        while iter.next:
            iter = iter.next
        return iter

    def Partition(self, par):
        lastElement = self.returnLast()
        previous = None
        current = self.head
        for i in range(self.lenght()-1):
            if current.k < par:
                if previous:
                    previous.next = current
                previous = current
            else:
                lastElement.next = current
                lastElement = lastElement.next
                if current is self.head:
                    self.head = current.next
            current = current.next

        lastElement.next = None
        if previous:
            if previous.next is not current:
                previous.next = current

        return self.head

    def print(self):
        iter = self.head
        while iter:
            print(iter.k)
            iter = iter.next


if __name__ == '__main__':
    a = Node(1)
    b = Node(2,a)
    c = Node(10,b)
    d = Node(5,c)
    e = Node(8,d)
    f = Node(5,e)
    g = Node(3,f)
    linkedList = LinkedList(g)
    linkedList.Partition(5)
    linkedList.print()
    print('\n')
    c = Node(10)
    d = Node(5, c)
    e = Node(8, d)
    f = Node(5, e)
    g = Node(3, f)
    linkedList = LinkedList(g)
    linkedList.Partition(5)
    linkedList.print()
    print('\n')
    c = Node(10)
    d = Node(5, c)
    e = Node(8, d)
    f = Node(5, e)
    g = Node(3, f)
    b = Node(8, g)
    linkedList = LinkedList(b)
    linkedList.Partition(5)
    linkedList.print()
    print('\n')
    c = Node(10)
    d = Node(5, c)
    e = Node(8, d)
    f = Node(5, e)
    g = Node(7, f)
    b = Node(8, g)
    linkedList = LinkedList(b)
    linkedList.Partition(5)
    linkedList.print()


class Node:
    def __init__(self,x, next=None):
        self.x = x
        self.next=next

class LinkedList:
    def __init__(self, head=None):
        self.head=head

    def isEmpty(self):
        if not self.head:
            return True

    def pushHead(self, node):
        if self.head:
            node.next=self.head
        self.head=node

def SumLists(L1, L2):
    if L1.isEmpty():
        return L2
    elif L2.isEmpty():
        return L1

    FirstIter = L1.head
    SecondIter = L2.head
    output=LinkedList()
    memory=0
    while FirstIter or SecondIter:
        L1value=0
        L2value=0
        if FirstIter:
            L1value = FirstIter.x
            FirstIter = FirstIter.next
        if SecondIter:
            L2value = SecondIter.x
            SecondIter = SecondIter.next
        value = (L1value+L2value+memory)%10
        memory = int((L1value+L2value+memory)/10)
        newNode = Node(value)
        if not output.head:
            output.head=newNode
            output_node=newNode
        else:
            output_node.next=newNode
            output_node=output_node.next
    if memory != 0:
        output_node.next = Node(memory)
    return output

class Stack:
    def __init__(self):
        self.data=[]

    def push(self,x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()

    def Empty(self):
        if not len(self.data):
            return True
        return False

def SumListsV2(L1,L2):
    if L1.isEmpty():
        return L2
    elif L2.isEmpty():
        return L1

    S1 = Stack()
    S2 = Stack()
    FirstIter = L1.head
    SecondIter = L2.head
    while FirstIter or SecondIter:
        if FirstIter:
            S1.push(FirstIter.x)
            FirstIter = FirstIter.next
        if SecondIter:
            S2.push(SecondIter.x)
            SecondIter = SecondIter.next
    output = LinkedList()
    memory = 0
    while (not S1.Empty()) or (not S2.Empty()):
        x1=0
        x2=0
        if not S1.Empty():
            x1 = S1.pop()
        if not S2.Empty():
            x2 = S2.pop()

        value = (x1+x2+memory)%10
        memory = int((x1+x2+memory)/10)
        output.pushHead(Node(value))
    if memory != 0:
        output.pushHead(Node(memory))
    return output

if __name__ == '__main__':
    a=Node(6)
    b=Node(1,a)
    c=Node(7,b)
    l1=LinkedList(c)

    d=Node(2)
    e=Node(9,d)
    f=Node(5,e)
    #g=Node(2,f)
    l2=LinkedList(f)
    output = SumLists(l1,l2)

    ite=output.head
    while ite:
        print(ite.x)
        ite=ite.next
    print('\n')

    a = Node(7)
    b = Node(1, a)
    c = Node(6, b)
    l1 = LinkedList(c)

    d = Node(5)
    e = Node(9, d)
    f = Node(2, e)
    g = Node(2, f)
    l2 = LinkedList(g)
    output = SumListsV2(l1, l2)

    ite = output.head
    while ite:
        print(ite.x)
        ite = ite.next
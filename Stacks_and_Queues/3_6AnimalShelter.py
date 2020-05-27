class Node:
    def __init__(self, x, next=None):
        self.x=x
        self.next=next

class LinkedList:
    def __init__(self, head=None):
        self.head=head
        self.tail=head

    def insert(self,x):
        newNode = Node(x)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode

    def popWhatever(self):
        x=False
        if self.head:
            x = self.head
            self.head=self.head.next
            if not self.head:
                self.tail=None
        return x

    def popSpecific(self, type):
        x=False
        if self.head and (type=='dog' or type=='cat'):
            if self.head.x == type:
                x = self.head.x
                self.head=self.head.next
                if not self.head:
                    self.tail = None
            else:
                itera = self.head
                while itera.next:
                    if itera.next.x == type:
                        x = itera.next.x
                        if itera.next == self.tail:
                            self.tail = itera
                        itera.next = itera.next.next
                        break
                    itera = itera.next
        return x

if __name__ == '__main__':
    linked = LinkedList()
    linked.insert('dog')
    linked.insert('cat')
    linked.insert('cat')
    linked.insert('dog')
    linked.insert('dog')
    linked.insert('cat')
    print(linked.popWhatever().x)
    print(linked.popWhatever().x)
    print(linked.popSpecific('dog'))
    print(linked.popSpecific('dog'))
    print(linked.popWhatever().x)
    print(linked.popSpecific('dog'))
    print(linked.popSpecific('cat'))
    linked.insert('dog')
    linked.insert('cat')
    print(linked.popWhatever().x)
    print(linked.popSpecific('dog'))
    print(linked.popSpecific('cat'))
    print(linked.popSpecific('cat'))
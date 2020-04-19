
class Node:
    def __init__(self, value):
        self.key = value
        self.next = None

class Linked_list:
    def __init__(self, input):
        self.head = input.pop(0)
        iter = self.head
        for item in input:
            iter.next = item
            iter = iter.next

def Linked_remove_duplicates(linked_list):
    memory = {linked_list.head.key : True}
    iter = linked_list.head
    while iter.next!=None:
        k=iter.next.key
        if memory.get(k):
            iter.next=iter.next.next
        else:
            memory[k]=True
            iter = iter.next

    return linked_list




if '__main__' == __name__:
    Nodes = [Node(2), Node(3), Node(2), Node(1), Node(3),
             Node(4),Node(5), Node(2), Node(1)]
    Linked_list = Linked_list(Nodes)

    ll = Linked_remove_duplicates(Linked_list)
    iter = ll.head
    while iter != None:
        print(iter.key)
        iter = iter.next
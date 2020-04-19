
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


def kth_toLast(linked_list, k):
    iter = linked_list.head
    runner = linked_list.head
    for i in range(0,k):
        if not runner:
            return False
        runner = runner.next
    while runner:
        runner = runner.next
        iter = iter.next
    return iter

if '__main__' == __name__:
    Nodes = [Node(2), Node(3), Node(1), Node(6), Node(4)]
    Linked_list = Linked_list(Nodes)

    print(kth_toLast(Linked_list, 2))
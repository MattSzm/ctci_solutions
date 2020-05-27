
class Node:
    def __init__(self, x, next=None):
        self.x = x
        self.next=next

#super slow
def LoopDetection(input):
    mainIte = input
    maxLenght = 0
    while True:
        currlengh = 0
        mainIte = mainIte.next
        helpIte = input
        while helpIte != mainIte:
            currlengh += 1
            helpIte = helpIte.next
        if currlengh < maxLenght:
            break
        maxLenght = currlengh
    return mainIte

def LoopDetectionMuchBetter(input):
    slower = input
    faster = input
    while faster and faster.next:
        slower = slower.next
        faster = faster.next.next
        if slower == faster:
            break

    if not faster or not faster.next:
        raise Exception

    slower = input
    while slower != faster:
        slower = slower.next
        faster = faster.next

    return faster


if __name__ == '__main__':
    e = Node('E')
    d = Node('D',e)
    c = Node('C',d)
    b = Node('B',c)
    a = Node('A',b)
    e.next = c

    output = LoopDetection(a)
    print(output.x)

    output = LoopDetectionMuchBetter(a)
    print(output.x)

class Node:
    def __init__(self, key):
        self.k = key
        self.min = None

class Stack:
    def __init__(self):
        self.data = []
        self.size = 0

    def append(self, key):
        node = Node(key)
        self.data.append(node)
        self.size += 1
        if self.size == 1:
            self.data[0].min = self.data[0].k
        else:
            min_value = min(self.data[self.size-1].k,self.data[self.size-2].min)
            self.data[self.size-1].min = min_value
        """else:
            if self.data[self.size-1].k < self.data[self.size-2].min:
                self.data[self.size-1].min = self.data[self.size-1].k
            else:
                self.data[self.size-1].min = self.data[self.size-2].min"""

    def extractMin(self):
        return self.data[self.size-1].min

    def pop(self):
        if self.size == 0:
            raise BaseException
        else:
            self.size -= 1
            return self.data.pop()

class BetterStack:
    def __init__(self):
        self.stack = []
        self.size = 0
        self.help = []
        self.helpSize = 0

    def append(self, key):
        self.stack.append(key)
        self.size += 1
        if self.size == 1:
            self.appendHelper(key)
        else:
            if key <= self.help[self.helpSize - 1]:
                self.appendHelper(key)

    def extractMin(self):
        return self.help[self.helpSize - 1]

    def appendHelper(self, key):
        self.help.append(key)
        self.helpSize += 1

    def pop(self):
        if self.size == 0:
            raise BaseException
        else:
            value = self.stack.pop()
            self.size -= 1
            if value == self.help[self.helpSize-1]:
                self.help.pop()
                self.helpSize -= 1
            return value


if '__main__' == __name__:
    stack = Stack()
    stack.append(4)
    stack.append(2)
    stack.append(6)
    stack.append(3)
    print(stack.extractMin())
    print(stack.pop().k)
    print(stack.pop().k)
    print(stack.pop().k)
    print(stack.extractMin())
    print(stack.pop().k)
    stack.append(1)
    stack.append(7)
    print(stack.extractMin())
    print('\n')
    stack = BetterStack()
    stack.append(4)
    stack.append(2)
    stack.append(6)
    stack.append(3)
    print(stack.extractMin())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.extractMin())
    print(stack.pop())
    stack.append(7)
    stack.append(1)
    stack.append(1)
    stack.pop()
    print(stack.extractMin())

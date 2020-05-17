import unittest

class Stack:
    def __init__(self):
        self.data = []

    def push(self,x):
        self.data.append(x)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[len(self.data)-1]

    def Empty(self):
        if len(self.data) == 0:
            return True
        return False

def SortStack(inputStack):
    if inputStack.Empty():
        return -1

    memoryStack = Stack()
    while not inputStack.Empty():
        x = inputStack.pop()
        counter = 0
        while not memoryStack.Empty():
            inputStack.push(memoryStack.pop())
            counter += 1
        while counter>0:
            if x and x<inputStack.peek():
                memoryStack.push(x)
                x=None
            else:
                memoryStack.push(inputStack.pop())
                counter -= 1
        if x:
            memoryStack.push(x)
    while not memoryStack.Empty():
        inputStack.push(memoryStack.pop())
    return inputStack

def SortStackBetter(inputStack):
    if inputStack.Empty():
        return -1

    memoryStack = Stack()
    while not inputStack.Empty():
        x = inputStack.pop()
        counter = 0
        while not memoryStack.Empty() and x < memoryStack.peek():
            inputStack.push(memoryStack.pop())
            counter += 1
        memoryStack.push(x)
        while counter>0:
            memoryStack.push(inputStack.pop())
            counter -= 1

    while not memoryStack.Empty():
        inputStack.push(memoryStack.pop())
    return inputStack


class tests(unittest.TestCase):
    inputStack = Stack()
    inputStack.push(5)
    inputStack.push(3)
    inputStack.push(7)
    inputStack.push(2)
    inputStack2 = Stack()

    expected = [2,3,5,7]

    inputStack3 = Stack()
    inputStack3.push(5)
    inputStack3.push(3)
    inputStack3.push(7)
    inputStack3.push(2)

    def test_True(self):
        output = SortStack(self.inputStack)
        for i in self.expected:
            self.assertEqual(i, output.pop())

        output = SortStackBetter(self.inputStack3)
        for i in self.expected:
            self.assertEqual(i, output.pop())


    def test_False(self):
        output = SortStack(self.inputStack2)
        self.assertEqual(output,-1)

if __name__ == '__main__':
    unittest.main()

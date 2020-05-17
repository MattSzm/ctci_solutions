import unittest

class Stack:
    def __init__(self):
        self.data = []
        self.size = 0

    def append(self, key):
        self.data.append(key)
        self.size += 1

    def pop(self):
        x = self.data.pop()
        self.size -= 1
        return x

class Stack_of_plates:
    def __init__(self, threshold):
        self.stacks = []
        self.t = threshold
        self.amount = 0

    def append(self, x):
        if (self.amount == 0 or
                self.stacks[self.amount-1].size == self.t):
            self.stacks.append(Stack())
            self.amount += 1
        self.stacks[self.amount-1].append(x)

    def pop(self):
        if self.amount == 0:
            raise ImportWarning
        x = self.stacks[self.amount-1].pop()
        if self.stacks[self.amount-1].size == 0:
            del self.stacks[self.amount-1]
            self.amount -= 1
        return x

    def popAt(self, index):
        if index < 0 or index >= self.amount:
            return False
        x = self.stacks[index].pop()
        if self.stacks[index].size == 0:
            del self.stacks[index]
            self.amount -= 1
        return x


class test(unittest.TestCase):
    def test_append_and_pop(self):
        my_stack = Stack_of_plates(2)
        my_stack.append(2)
        my_stack.append(5)
        my_stack.append(1)
        my_stack.append(3)

        expected = [3,1,5,2]
        output = []
        for i in range(4):
            output.append(my_stack.pop())
        self.assertEqual(expected, output)

    def test_popAt(self):
        my_stack = Stack_of_plates(2)
        my_stack.append(2)
        my_stack.append(5)
        my_stack.append(1)
        my_stack.append(3)

        expected = [5,2]
        output = []
        for i in range(2):
            output.append(my_stack.popAt(0))
        self.assertEqual(expected,output)

        output = my_stack.popAt(2)
        self.assertFalse(output)


if '__main__' == __name__:
    unittest.main()

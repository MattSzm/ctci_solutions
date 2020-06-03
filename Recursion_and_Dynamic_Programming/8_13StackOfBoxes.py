import unittest

class Box:
    def __init__(self, w, d, h):
        self.w = w
        self.d = d
        self.h = h

def isBigger(bigger, smaller):
    if bigger.w > smaller.w and bigger.d > smaller.d:
        return True
    return False

def StackOfBoxes(input):
    input.sort(key=lambda x: x.h, reverse=True)
    memory = [input[0].h]
    output = input[0].h
    for curr in range(1, len(input)):
        biggest = input[curr].h
        for i in range(curr-1,-1,-1):
            if isBigger(input[i], input[curr]):
                if input[curr].h + memory[i] > biggest:
                    biggest = input[curr].h + memory[i]
        memory.append(biggest)
        output = max(biggest, output)
    return output


class tests(unittest.TestCase):
    a = Box(10,10,5)
    b = Box(9,8,6)
    c = Box(7,7,2)
    d = Box(6,4,4)
    e = Box(4,3,2)
    f = Box(4,2,3)
    g = Box(5,5,1)
    inputOne = [b,d,a,f,g,e,c]
    expectedOne = 13

    a = Box(5,5,10)
    b = Box(4,3,8)
    c = Box(10,8,8)
    d = Box(8,4,5)
    e = Box(6,3,4)
    f = Box(3,2,2)
    inputTwo = [a,c,e,b,f,d]
    expectedTwo = 20

    def test_One(self):
        output = StackOfBoxes(self.inputOne)
        self.assertEqual(output, self.expectedOne)

    def test_Two(self):
        output = StackOfBoxes(self.inputTwo)
        self.assertEqual(output, self.expectedTwo)

if __name__ == '__main__':
    unittest.main()
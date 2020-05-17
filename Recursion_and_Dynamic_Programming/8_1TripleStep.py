import unittest

def TripleStep(inputSize):
    if inputSize == 0:
        return 1
    if inputSize > 0 and inputSize <= 2:
        return inputSize
    memory = [0 for _ in range(inputSize+1)]
    memory[0] = 1
    memory[1] = 1
    for i in range(2, inputSize+1):
        memory[i] = memory[i-1]+memory[i-2]+memory[i-3]
    return memory[inputSize]

class tests(unittest.TestCase):
    data = [
        (0,1),
        (1,1),
        (2,2),
        (3,4),
        (4,7),
        (5,13)
    ]

    def test_True(self):
        for [input, expected] in self.data:
            output = TripleStep(input)
            self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
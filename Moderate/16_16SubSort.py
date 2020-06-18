import unittest

def OneAndOnly(input:list):
    sortedInput = sorted(input)
    found = False

    start = -1
    end = -1
    for index in range(len(input)):
        if input[index] != sortedInput[index] and not found and end != -1:
            found = True
        elif input[index] != sortedInput[index] and not found:
            start = index
            found = True
        elif input[index] == sortedInput[index] and found:
            end = index - 1
            found = False

    return start, end


class tests(unittest.TestCase):
    data = [
        ([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19], 3, 9),
            ([1,2,8,4,3,9,7,12,15],2,6)
        ]


    def test_working(self):
        for [input, startExpected, endExpected] in self.data:
            start, end = OneAndOnly(input)
            self.assertEqual(start, startExpected)
            self.assertEqual(end, endExpected)


if __name__ == '__main__':
    unittest.main()

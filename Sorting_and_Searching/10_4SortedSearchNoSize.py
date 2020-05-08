def SortedSearchNoSize(input, x):
    size = 1
    if input[size] != -1 and input[size] < x:
        size *= 2
    right = size
    left = int(size/2)

    while left <= right:
        m = int((right+left)/2)
        if x == input[m]:
            return m
        elif input[m] == -1 or x < input[m]:
            right = m - 1
        else:
            left = m + 1
    return -1

import unittest

class tests(unittest.TestCase):
    data = [
        ([1,3,4,6,8,-1,-1,-1,-1,-1,-1,-1],6,3),
        ([1,1,3,4,6,6,7,8,9,10,13,15 -1, -1, -1, -1, -1, -1, -1], 13, 10),
    ]
    def sortedtest(self):
        for [input,search,expected] in self.data:
            output = SortedSearchNoSize(input,search)
            self.assertEqual(output,expected)

if __name__ == '__main__':
    unittest.main()
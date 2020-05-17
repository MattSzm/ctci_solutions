import unittest
def MagicIndexBase(arr):
    return MagicIndex(arr, 0, len(arr)-1)

def MagicIndex(arr, p, q):
    if q < p:
        return False
    m = int((p+q)/2)
    if arr[m] == m:
        return m
    elif arr[m] < m:
        return MagicIndex(arr, m+1, q)
    else:
        return MagicIndex(arr, p, m-1)

def MagincIndexBetterBase(arr):
    return MagicIndexBetter(arr, 0, len(arr)-1)

def MagicIndexBetter(arr, p, q):
    if q < p:
        return -1
    m_index = int((p+q)/2)
    m_value = arr[m_index]
    if m_value == m_index:
        return m_value

    left_index = min(m_value, m_index - 1)
    left = MagicIndexBetter(arr, p, left_index)
    if left >= 0:
        return left

    right_index = max(m_value, m_index + 1)
    right = MagicIndexBetter(arr, right_index, q)
    return right

class tests(unittest.TestCase):
    dataT = [
        ([-5,-2,0,1,3,5,8], 5),
        ([-3,0,2,5,7,8], 2),
    ]
    dataF = [
        [-3,-2,-1,0,2,3]
    ]
    dataTBetter = [
        ([-3,0,2,4,6,6,6,6,10],6),
        ([-2,0,1,2,6,6,8,8,9,9], 9),
        ([-2,-2,-2,0,7,7,7,9], -1),
    ]

    def test_True(self):
        for [input, expected] in self.dataT:
            output = MagicIndexBase(input)
            self.assertEqual(output,expected)
        for [input, expected] in self.dataTBetter:
            output = MagincIndexBetterBase(input)
            self.assertEqual(output, expected)

    def test_False(self):
        for input in self.dataF:
            output = MagicIndexBase(input)
            self.assertFalse(output)


if '__main__' == __name__:
    unittest.main()
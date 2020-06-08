import unittest

def countFives(intput:int)-> int:
    count = 0
    while intput%5==0:
        count += 1
        intput /= 5
    return count


def FactororialZeros(intput:int)->int:
    if intput < 5:
        return 0
    count = 0
    for i in range(5, intput+1):
        count += countFives(i)

    return count

class tests(unittest.TestCase):
    data = [
        (5,1),
        (13,2),
        (26,6),
        (3,0),
    ]

    def test_working(self):
        for [input, expected] in self.data:
            output = FactororialZeros(input)
            self.assertEqual(expected, output)

if __name__ == '__main__':
    unittest.main()
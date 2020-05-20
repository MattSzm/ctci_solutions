import unittest

def Conversion(first, second):
    if first == second:
        return 0
    elif first > second:
        bigger=first
        smaller=second
    else:
        bigger=second
        smaller=first

    counter = 0
    while bigger>0 and smaller>0:
        if bigger&1 != smaller&1:
            counter += 1
        bigger >>= 1
        smaller >>= 1
    while bigger > 0:
        counter += bigger&1
        bigger >>= 1
    return counter

def ConversionBetter(first, second):
    xorOperation = first^second
    counter = 0
    while xorOperation > 0:
        counter += xorOperation&1
        xorOperation >>=1
    return counter


class tests(unittest.TestCase):
    data = [
        (29,15,2),
        (11,713,4)
    ]

    def test_working(self):
        for [first, second, expected] in self.data:
            output = Conversion(first, second)
            self.assertEqual(output, expected)

    def test_working_better(self):
        for [first, second, expected] in self.data:
            output = ConversionBetter(first, second)
            self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
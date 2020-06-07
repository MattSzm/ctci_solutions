import unittest

def NumberSwapper(a, b):
    a = a-b
    b = b+a
    a = b-a
    return a,b

def NumberSwapperbit(a, b):
    a = a^b
    b = a^b
    a = a^b
    return a, b

class tests(unittest.TestCase):
    data1 = [
        (3, 7),
        {5, 1}
    ]
    data2 = [
        (3, 7),
        {5, 1}
    ]

    def test_one(self):
        for first, second in self.data1:
            b,a = NumberSwapper(first, second)
            self.assertEqual(first,a)
            self.assertEqual(second,b)

    def test_two(self):
        for first, second in self.data2:
            b,a = NumberSwapper(first, second)
            self.assertEqual(first,a)
            self.assertEqual(second,b)


if __name__ == '__main__':
    unittest.main()
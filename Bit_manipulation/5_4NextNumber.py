import unittest
import sys

def NextNumber(input):
    if input==0:
        return False

    c = input
    c1 = 0
    c0 = 0
    while c&1==0 and c!=0:
        c0 += 1
        c >>= 1

    while c&1==1:
        c1 += 1
        c >>= 1

    p = c1 + c0
    input = input|(1 << p)

    mask = 1<<p
    mask -= 1
    mask = ~mask
    input = input&mask

    secondmask = 1<<c1-1
    secondmask -= 1
    input |= secondmask

    return input

def PreviousNumber(input):
    if input == 0:
        return False

    c = input
    c1 = 0
    c0 = 0
    while c&1 == 1:
        c1 += 1
        c >>= 1

    while c&1 == 0:
        c0 += 1
        c >>= 1

    p = c0 + c1
    input &= ~(1<<p)
    input |= 1<<p-1
    mask = 1<<p-1
    mask -= 1
    input |= mask
    secondmask = ~0
    secondmask <<= c0-1
    input &= secondmask

    return input

class test(unittest.TestCase):
    dataNext = [
        (13948, 13967),
    ]
    dataPrevious = [
        (10115,10096),
    ]

    def test(self):
        for [input, expected] in self.dataNext:
            output = NextNumber(input)
            self.assertEqual(output,expected)
        for [input, expected] in self.dataPrevious:
            output = PreviousNumber(input)
            self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()
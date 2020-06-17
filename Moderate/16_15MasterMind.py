import unittest

def algo(input:str, attempt:str):
    if len(input) != len(attempt):
        return -1, -1
    hitCount = 0
    pseudoHitCount = 0
    memoryOfInput = {}

    for index in range(len(input)):
        if input[index] == attempt[index]:
            hitCount += 1
        else:
            if memoryOfInput.get(input[index]):
                memoryOfInput[input[index]] += 1
            else:
                memoryOfInput[input[index]] = 1

    for value in attempt:
        if value in memoryOfInput:
            if memoryOfInput[value] > 0:
                pseudoHitCount += 1
                memoryOfInput[value] -= 1

    return hitCount, pseudoHitCount

class tests(unittest.TestCase):
    data = (
            ['ABCA','CAAD',0,3],
            ['RGBY','GGRR', 1,1],
            ['RGBBA','AADG',-1,-1]
            )

    def test_working(self):
        for [input, attempt, hitExpected, pseudoHitExpected] in self.data:
            hit, pseudoHit = algo(input, attempt)
            self.assertEqual(hit, hitExpected)
            self.assertEqual(pseudoHit, pseudoHitExpected)


if __name__ == '__main__':
    unittest.main()
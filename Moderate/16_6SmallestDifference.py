import sys
import unittest

def SmallestDiff(arrayOne:list, arrayTwo:list)->int:
    if len(arrayOne) == 0 or len(arrayTwo) == 0:
        return 0

    arrayOne.sort()
    arrayTwo.sort()
    iterOne = 0
    iterTwo = 0
    best = sys.maxsize
    while iterOne < len(arrayOne) and  iterTwo < len(arrayTwo):
        if arrayOne[iterOne] == arrayTwo[iterTwo]:
            return 0
        elif arrayOne[iterOne] > arrayTwo[iterTwo]:
            diff = arrayOne[iterOne] - arrayTwo[iterTwo]
            iterTwo += 1
        else:
            diff = arrayTwo[iterTwo] - arrayOne[iterOne]
            iterOne += 1
        best = min(best, diff)

    return best


class tests(unittest.TestCase):
    data = [
        ([1,4,2,9,2],[-2,10,7,13],1),
        ([-10,5,-5,1],[-20,-9,2,3,4,6],1),
        ([-20,30,5,46,256,13],[-4,3,48,1,35,46,89,463,1],0),
        ([-5,0,15,17],[12,5,27,-9],3)
    ]

    def test_working(self):
        for [arrayOne, arrayTwo, expected] in self.data:
            output = SmallestDiff(arrayOne, arrayTwo)
            self.assertEqual(output, expected)


if __name__ == '__main__':
    unittest.main()
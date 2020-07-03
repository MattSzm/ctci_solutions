import unittest

def SumSwap(arrayOne, arrayTwo):
    if sum(arrayOne) > sum(arrayTwo):
        biggerArray = arrayOne
        smallerArray = arrayTwo
    else:
        biggerArray = arrayTwo
        smallerArray = arrayOne
    biggerSum = sum(biggerArray)
    smallerSum = sum(smallerArray)
    output = []

    redundancy = biggerSum - smallerSum
    if redundancy == 0:
        return output
    elif redundancy%2 == 1:
        return -1

    goal = redundancy/2
    biggerArray.sort()
    smallerArray.sort()

    smallerIndex = 0
    biggerIndex = 0
    while biggerIndex < len(biggerArray):
        if biggerArray[biggerIndex] >= goal:
            break
        biggerIndex += 1


    while biggerIndex < len(biggerArray) and smallerIndex < len(smallerArray):
        if biggerArray[biggerIndex] - smallerArray[smallerIndex] == goal:
            output = [biggerArray[biggerIndex], smallerArray[smallerIndex]]
            break
        elif biggerArray[biggerIndex] - smallerArray[smallerIndex] > goal:
            smallerIndex += 1
        else:
            biggerIndex += 1
    return output


class teste(unittest.TestCase):
    data = (
        [[4, 1, 2, 1, 1, 2], [3, 6, 3, 3], [3, 1]],
        [[4, 1, 2, 1, 1, 0], [3, 6, 5, 3], [5, 1]],
        [[4,2,1],[1,1,3,2],[]],
    )
    dataNotWorking = (
        [[2,1,5,2],[4,1,7,3]],
    )

    def test_working(self):
        for [arrayOne, arrayTwo, expected] in self.data:
            output = SumSwap(arrayOne, arrayTwo)
            self.assertListEqual(output,expected)

    def test_notWorking(self):
        for [arrayOne, arrayTwo] in self.dataNotWorking:
            output = SumSwap(arrayOne, arrayTwo)
            self.assertEqual(output,-1)

if __name__ == '__main__':
    unittest.main()
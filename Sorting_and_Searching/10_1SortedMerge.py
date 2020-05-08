import unittest

def Merge(firstArray, secondArray):
    fl = len(firstArray)
    sl = len(secondArray)
    helper = []
    for i in firstArray:
        helper.append(i)
    for i in secondArray:
        helper.append(i)
        firstArray.append(0)

    Mindex=0
    Lindex=0
    Rindex=fl
    while Lindex < fl and Rindex < fl+sl:
        if helper[Lindex] < helper[Rindex]:
            firstArray[Mindex] = helper[Lindex]
            Lindex += 1
        else:
            firstArray[Mindex] = helper[Rindex]
            Rindex += 1
        Mindex += 1

    while Lindex < fl:
        firstArray[Mindex] = helper[Lindex]
        Mindex += 1
        Lindex += 1
    while Rindex < fl+sl:
        firstArray[Mindex] = helper[Rindex]
        Mindex += 1
        Rindex += 1
    return firstArray

def Mergev2(firstArray, secondArray):
    fl = len(firstArray)
    sl = len(secondArray)
    for i in range(sl):
        firstArray.append(0)
    firstIndex = fl-1
    secondIndex = sl-1
    MergeIndex = len(firstArray)-1

    while secondIndex >=0 :
        if firstIndex >= 0 and firstArray[firstIndex] > secondArray[secondIndex]:
            firstArray[MergeIndex] = firstArray[firstIndex]
            firstIndex -= 1
        else:
            firstArray[MergeIndex] = secondArray[secondIndex]
            secondIndex -= 1
        MergeIndex -= 1
    return firstArray

class tests(unittest.TestCase):
    data = [
        ([1,4,7,8,10], [2,3,3,4,11], [1,2,3,3,4,4,7,8,10,11])
    ]
    datav2 = [
        ([1, 4, 7, 8, 10], [2, 3, 3, 4, 11], [1, 2, 3, 3, 4, 4, 7, 8, 10, 11])
    ]

    def test(self):
        for [A, B, expected] in self.data:
            result = Merge(A, B)
            self.assertEqual(expected, result)
        for [A, B, expected] in self.datav2:
            result = Mergev2(A, B)
            self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()

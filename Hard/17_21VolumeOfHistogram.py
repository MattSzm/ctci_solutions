import unittest

def Volume(input):
    index = 0
    length = len(input)
    while input[index] == 0:
        index += 1
        if index == length:
            return -1

    output = 0
    while index < length:
        if input[index] > 0:
            if index + 1 == length:
                break
            maxMemo = {'index': None, 'value':0}
            for j in range(index+1, length, 1):

                if input[j] >= input[index]:
                    maxMemo = {'index': j, 'value': input[j]}
                    break
                else:
                    if input[j] >= maxMemo['value']:
                        maxMemo = {'index': j, 'value': input[j]}

            output += addWater(input, index, maxMemo['index'])
            index = maxMemo['index']
        else:
            index += 1

    return output

def addWater(input, leftIndex, rightIndex):
    output = 0
    minValue = min(input[leftIndex], input[rightIndex])
    for index in range(leftIndex+1, rightIndex, 1):
        output += minValue - input[index]
    return output


def SecondOption(input):
    indexLeft = 0
    length = len(input)
    while input[indexLeft] == 0:
        indexLeft += 1
        if indexLeft == length:
            return -1

    indexRight = length - 1
    while input[indexRight] == 0:
        indexRight -= 1

    output = 0
    height =  1
    while indexLeft < indexRight:
        for ite in range(indexLeft+1, indexRight):
            if height > input[ite]:
                output += 1
        height += 1
        while height > input[indexLeft]:
            indexLeft += 1
        while height > input[indexRight]:
            indexRight -= 1

    return output

class tests(unittest.TestCase):
    data = (
        ([0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 5, 0, 1, 0, 0, 0],26),
        ([2,0,0,4,0,1,6,3,0,2],13),
        ([0,0,0,0,1,0,0,3,0,3,0,4,0,3,0,7,0,0,0],17),
        ([0,0,0,0,0,0],-1)
    )

    def test_first(self):
        for [input, expected] in self.data:
            output = Volume(input)
            self.assertEqual(output,expected)

    def test_second(self):
        for [input, expected] in self.data:
            output = SecondOption(input)
            self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()



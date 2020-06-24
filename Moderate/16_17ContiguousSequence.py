
def recursion(input:list, left:int, right:int):
    if left == right:
        return input[left], left, right
    middle = int((left+right)/2)
    maxLeft, leftLeft, rightLeft = recursion(input, left, middle)
    maxRight, leftRight, rightRight = recursion(input, middle+1, right)
    maxMerge, leftMerge, rightMerge = Merge(input, left, right, middle)

    if maxLeft>maxMerge and maxLeft>maxRight:
        return maxLeft, leftLeft, rightLeft
    elif maxRight>maxMerge and maxRight>maxLeft:
        return maxRight, leftRight, rightRight
    else:
        return maxMerge, leftMerge, rightMerge


def Merge(input:list, left:int, right:int, middle:int):
    leftSubValue = input[middle]
    rightSubValue = input[middle]
    leftIndex = middle
    rightIndex = middle

    subCurrent = input[middle]
    for i in range(middle-1, left-1, -1):
        subCurrent += input[i]
        if subCurrent > leftSubValue:
            leftSubValue = subCurrent
            leftIndex = i

    subCurrent = input[middle]
    for i in range(middle+1, right+1, 1):
        subCurrent += input[i]
        if subCurrent > rightSubValue:
            rightSubValue = subCurrent
            rightIndex = i

    return leftSubValue + rightSubValue - input[middle], leftIndex, rightIndex

def Sequence(input):
    if len(input) == 0:
        return -1
    if len(input) == 1:
        return input[0]
    value, leftIndex, rightIndex = recursion(input, 0, len(input)-1)
    return input[leftIndex:rightIndex+1], value


if __name__ == '__main__':
    input = [2, -8, 3, -2, 4, -10]
    outputSeq, outputValue = Sequence(input)
    print(outputSeq)
    print(outputValue)
    print('\n')

    input2 = [13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
    output2Seq, output2Value = Sequence(input2)
    print(output2Seq)
    print(output2Value)

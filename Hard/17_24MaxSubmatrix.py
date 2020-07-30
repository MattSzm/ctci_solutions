import sys

def MaxSubMatrix(matrix):
    output = -sys.maxsize
    for upper in range(len(matrix)):
        memo = [0]*len(matrix[0])
        for bottom in range(upper, len(matrix)):
            for columnIndex in range(len(matrix[0])):
                memo[columnIndex] += matrix[bottom][columnIndex]
            currOutput = maxSub(memo)
            output = max(output, currOutput)
    return output

def maxSub(input):
    maxvalue = -sys.maxsize
    currValue = 0
    for el in input:
        currValue += el
        if currValue > maxvalue:
            maxvalue = currValue

        if currValue < 0:
            currValue = 0
    return maxvalue


if __name__ == '__main__':
    input = [[9,-8,1,3,-2],
             [-3,7,6,-2,4],
             [6,-4,-4,8,-7],
             [-2,1,-5,0,3]]
    print(MaxSubMatrix(input))

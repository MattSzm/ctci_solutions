def MaxSquare(matrix):
    length = len(matrix)
    maxOutput = 0
    for xIndex in range(length):
        for yIndex in range(length):
            if matrix[yIndex][xIndex] == 'b':
                currOutput = 1
                currX = xIndex + 1
                currY = yIndex + 1
                while currX < length and currY < length:
                    if (matrix[yIndex][currX] == 'b'
                            and matrix[currY][xIndex] == 'b'):
                        flag = False
                        for i in range(xIndex, currX + 1):
                            if matrix[currY][i] == 'white':
                                flag = True
                                break
                        if not flag:
                            for i in range(yIndex, currY + 1):
                                if matrix[i][currX] == 'white':
                                    flag = True
                                    break
                        if not flag:
                            currOutput = (currX - xIndex) ** 2
                        currX += 1
                        currY += 1
                    else:
                        break
                maxOutput = max(maxOutput, currOutput)
    return maxOutput


if __name__ == '__main__':
    input1 = [['b', 'w', 'w', 'w', 'b'],
              ['w', 'b', 'b', 'b', 'b'],
              ['b', 'b', 'w', 'b', 'w'],
              ['w', 'b', 'b', 'b', 'b'],
              ['w', 'b', 'w', 'w', 'w']]
    output = MaxSquare(input1)
    print(output)
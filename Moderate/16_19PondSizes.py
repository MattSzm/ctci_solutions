
def PondSizes(matrix):
    mSize = len(matrix)
    nSize = len(matrix[0])
    output = []
    for mIte in range(mSize):
        for nIte in range(nSize):
            singleOutput = Recur(matrix, mIte, nIte, mSize, nSize)
            if singleOutput > 0:
                output.append(singleOutput)

    return output

def Recur(matrix, mIte, nIte, mSize, nSize):
    if (mIte < 0 or mIte >= mSize) or (nIte < 0 or nIte >= nSize):
        return 0
    elif matrix[mIte][nIte] != 0:
        return 0
    else:
        matrix[mIte][nIte] = -1
        singleOutput = 1
        for i in range(-1,2,1):
            for j in range(-1,2,1):
                if not (i==0 and j==0):
                    singleOutput += Recur(matrix, mIte+i, nIte+j, mSize, nSize)
        return singleOutput


if __name__ == '__main__':
    input = [
        [0,2,1,0],
        [0,1,0,1],
        [1,1,0,1],
        [0,1,0,1]
    ]
    output = PondSizes(input)
    print(output)
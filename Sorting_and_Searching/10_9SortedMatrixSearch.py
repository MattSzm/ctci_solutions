

def SearchMatrix(matrix, IofN, JofN, IofM, JofM, x):
    if IofN>JofN or IofM>JofM:
        return False, False
    MiddleofN = int((IofN+JofN)/2)
    MiddleofM = int((IofM+JofM)/2)
    if matrix[MiddleofN][MiddleofM] == x:
        return MiddleofN, MiddleofM
    elif x > matrix[MiddleofN][MiddleofM]:
        IfromSameRow, JfromSameROw = SearchMatrix(matrix, IofN, JofN, MiddleofM+1, JofM, x)
    else:
        IfromSameRow, JfromSameROw = SearchMatrix(matrix, IofN, JofN, IofM, MiddleofM -1, x)

    IfromUp = False
    JfromUp = False
    IfromDown = False
    JfromDown = False
    if not(IfromSameRow or JfromSameROw):
        IfromUp, JfromUp = SearchMatrix(matrix, MiddleofN+1,JofN,  IofM, JofM, x)
        IfromDown, JfromDown = SearchMatrix(matrix, IofN, MiddleofN-1, IofM, JofM, x)

    return IfromSameRow|IfromUp|IfromDown, JfromSameROw|JfromUp|JfromDown

def SearchMatrixWrapper(matrix, x):
    return SearchMatrix(matrix, 0, len(matrix)-1, 0, len(matrix[0])-1, x)

def SearchMatrixBetter(matrix, x):
    row = 0
    column = len(matrix[0])-1
    while column >= 0 and row < len(matrix):
        if x == matrix[row][column]:
            return row, column
        elif x > matrix[row][column]:
            row += 1
        else:
            column -= 1
    return False, False

if __name__ == '__main__':
    matrix = [
        [1,5,6,13],
        [2,6,10,15],
        [4,7,12,18],
    ]
    indexOne, indexTwo = SearchMatrixWrapper(matrix, 12)
    print(str(indexOne) + ' ' + str(indexTwo))

    indexOne, indexTwo = SearchMatrixBetter(matrix, 12)
    print(str(indexOne) + ' ' + str(indexTwo))
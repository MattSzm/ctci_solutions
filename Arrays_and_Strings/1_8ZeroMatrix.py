
def ZeroMatrix(matrix):
    firstColumnHasZero = False
    firstRowHasZero = False
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            firstColumnHasZero=True
            break
    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            firstRowHasZero=True
            break

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            ZeroRow(matrix,i)

    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            ZeroColumn(matrix,i)

    if firstColumnHasZero:
        ZeroColumn(matrix,0)

    if firstRowHasZero:
        ZeroRow(matrix,0)

    return matrix


def ZeroRow(matrix, index):
    for i in range(len(matrix[0])):
        matrix[index][i] = 0

def ZeroColumn(matrix, index):
    for i in range(len(matrix)):
        matrix[i][index] = 0


if __name__ == '__main__':
    matrix = [
        [1,0,3,5],
        [0,6,9,4],
        [9,0,6,8],
        [9,4,1,5]
    ]

    output=ZeroMatrix(matrix)
    for i in output:
        print(i)
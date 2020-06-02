import copy

def eightQueens(row, columns, output):
    if row >= 8:
        output.append(columns)
    for i in range(8):
        copyOfColumns = copy.copy(columns)
        if isValid(row, columns, i):
            copyOfColumns.append(i)
            eightQueens(row+1, copyOfColumns, output)

def isValid(currRow, setColumns, columnIWant):
    for i in range(0,currRow):
        columnMemory = setColumns[i]

        if columnMemory == columnIWant:
            return False

        diff = abs(columnIWant-columnMemory)
        if diff == currRow-i:
            return False

    return True

def QueensWrapper():
    output = []
    eightQueens(0, [], output)
    return output

if __name__ == '__main__':
    output = QueensWrapper()
    for i in output:
        print(i)

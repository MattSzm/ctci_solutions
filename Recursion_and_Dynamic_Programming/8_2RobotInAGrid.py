class point:
    def __init__(self,i,j):
        self.i = i
        self.j = j

def Robot(Grid, row, column, movedRight, output=None):
    if row == 0  and column == 0:
        output = []
    output.append(point(row,column))
    if row == len(Grid) - 1 and column == len(Grid[0]) - 1:
        return output

    if len(Grid)-1 == row or not Grid[row+1][column]:
        return Robot(Grid, row, column+1, True, output)
    elif len(Grid[0])-1 == column or not Grid[row][column+1]:
        return Robot(Grid, row+1, column, False, output)
    elif movedRight:
        return Robot(Grid, row+1, column, False, output)
    else:
        return Robot(Grid, row, column+1, True, output)
if __name__ == '__main__':
    rows = 6
    column = 8
    inputGrid = [[True for _ in range(column)] for __ in range(rows)]
    inputGrid[1][0] = False
    inputGrid[1][1] = False
    inputGrid[2][2] = False
    inputGrid[2][3] = False
    inputGrid[3][3] = False
    inputGrid[3][4] = False
    inputGrid[5][5] = False
    inputGrid[4][5] = False
    inputGrid[4][6] = False
    output = Robot(inputGrid, 0, 0, False)

    for i in output:
        print(str(i.i) + '\t' + str(i.j))
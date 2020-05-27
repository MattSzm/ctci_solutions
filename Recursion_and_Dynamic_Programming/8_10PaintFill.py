
def PaintFill(screen:list, row:int, column:int, color:str)->bool:
    if not color in ['green', 'blue', 'yellow', 'red'] or \
            screen[row][column]==color:
        return False
    return PaintFillRecursive(screen, row, column, color, screen[row][column])


def PaintFillRecursive(screen:list, row:int, column:int, color:str, currentColor:str)->bool:
    if row<0 or row>len(screen)-1 or column<0 or column>len(screen[row])-1:
        return False
    if currentColor == screen[row][column]:
        screen[row][column] = color
        PaintFillRecursive(screen, row - 1, column, color, currentColor)
        PaintFillRecursive(screen, row + 1, column, color, currentColor)
        PaintFillRecursive(screen, row, column - 1, color, currentColor)
        PaintFillRecursive(screen, row, column + 1, color, currentColor)
    return True

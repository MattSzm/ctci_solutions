import random

class Square:
    def __init__(self):
        #black-1
        #white-0
        self.color = random.randint(0,1)

    def __repr__(self):
        return str(self.color)

    def swapColor(self):
        if self.color == 1:
            self.color = 0
        else:
            self.color = 1


class Grid:
    def __init__(self):
        self.grid = [[Square()]]

    def addRowUp(self):
        self.grid.insert(0, [Square() for _ in range(len(self.grid[0]))])
    def addRowDown(self):
        self.grid.append([Square() for _ in range(len(self.grid[0]))])

    def addColumnLeft(self):
        for i in range(len(self.grid)):
            self.grid[i].insert(0,Square())
    def addColumnRight(self):
        for i in range(len(self.grid)):
            self.grid[i].append(Square())

    def print(self):
        for row in self.grid:
            print(row)

    def printKMoves(self, k):
        position = 'right'

        mainIter = 0
        currX = 0
        currY = 0
        while mainIter < k:
            currSquare = self.grid[currY][currX]
            currSquare.swapColor()
            if currSquare.color == 1:
                position = self.changePosition(position)
            else:
                position = self.changePosition(position, False)

            if position == 'right':
                currX += 1
                if currX == len(self.grid[currY]):
                    self.addColumnRight()
            elif position == 'left':
                currX -= 1
                if currX == -1:
                    self.addColumnLeft()
                    currX = 0
            elif position == 'down':
                currY += 1
                if currY == len(self.grid):
                    self.addRowDown()
            else:
                currY -= 1
                if currY == -1:
                    self.addRowUp()
                    currY = 0
            mainIter += 1
        self.print()
        return currX, currY

    def changePosition(self, current, right=True):
        if right:
            if current == 'right':
                return 'down'
            elif current == 'down':
                return 'left'
            elif current == 'left':
                return 'up'
            else:
                return 'right'
        else:
            if current == 'right':
                return 'up'
            elif current == 'up':
                return 'left'
            elif current == 'left':
                return 'down'
            else:
                return 'right'


if __name__ == '__main__':
    grid = Grid()
    x,y = grid.printKMoves(130)

class Line:
    def __init__(self, sx,sy,ex,ey):
        self.startX = sx
        self.startY = sy
        self.endX = ex
        self.endY = ey
        self.a = None
        self.b = None

    @property
    def biggerX(self):
        if self.startX >= self.endX:
            return self.startX
        return self.endX

    @property
    def smallerX(self):
        if self.startX < self.endX:
            return self.startX
        return self.endX

    @property
    def biggerY(self):
        if self.startY >= self.endY:
            return self.startY
        return self.endY

    @property
    def smallerY(self):
        if self.startY < self.endY:
            return self.startY
        return self.endY

def equation(line):
    line.a = float((line.endY-line.startY)/
              (line.endX-line.startX))
    line.b = float(line.startY-line.a*line.startX)

def Intersection(lineOne, lineTwo):
    if not lineOne or not lineTwo:
        return False
    equation(lineOne)
    equation(lineTwo)
    if lineOne.a == lineTwo.a:
        if (lineOne.b == lineTwo.b and ((lineTwo.smallerX>=lineOne.smallerX and
            lineTwo.smallerX<=lineOne.biggerX) or(lineOne.smallerX>=lineTwo.smallerX
                                         and lineOne.smallerX<=lineTwo.biggerX))):
            return True
        return False
    interX = float((lineTwo.b-lineOne.b)/
                   (lineOne.a-lineTwo.a))
    interY = float(interX*lineOne.a +lineOne.b)
    if (not interX >= lineOne.smallerX) or (not interX >= lineTwo.smallerX):
        return False
    if (not interX <= lineOne.biggerX) or (not interX <= lineTwo.biggerX):
        return False
    if (not interY >= lineOne.smallerY) or (not interY >= lineTwo.smallerY):
        return False
    if (not interY <= lineOne.biggerY) or (not interY <= lineTwo.biggerY):
        return False

    return (interX, interY)

if __name__ == '__main__':
    #y=3x+3
    lineOne = Line(-2, -3, 1, 6)
    #y=-4x+5
    lineTwo = Line(0,5,3,-7)
    output = Intersection(lineOne, lineTwo)
    print(output)

    lineTree = Line(0,0,5,5)
    lineFour = Line(1,0,6,5)
    output = Intersection(lineTree,lineFour)
    print(output)

    line5 = Line(1,8,3,12)
    line6 = Line(2,10,4,14)
    output = Intersection(line5, line6)
    print(output)
    line7 = Line(4, 14, 6, 18)
    output = Intersection(line5, line7)
    print(output)
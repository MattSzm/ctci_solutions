
class TowerOfHanoi:
    def __init__(self, input=None):
        if not input:
            self.TowerOne = []
        else:
            self.TowerOne = input
        self.TowerTwo = []
        self.TowerThree = []


    def MoveRight(self, n):
        if n == 1:
            self.TowerThree.append(self.TowerOne.pop())
        else:
            self.MoveRight(n-1)
            #move n middle
            self.TowerTwo.append(self.TowerOne.pop())
            self.MoveLeft(n-1)
            # move n right
            self.TowerThree.append(self.TowerTwo.pop())
            self.MoveRight(n-1)

    def MoveLeft(self, n):
        if n == 1:
            self.TowerOne.append(self.TowerThree.pop())
        else:
            self.MoveLeft(n-1)
            #move n middle
            self.TowerTwo.append(self.TowerThree.pop())
            self.MoveRight(n-1)
            #move n left
            self.TowerOne.append(self.TowerTwo.pop())
            self.MoveLeft(n-1)

    def algo(self):
        self.MoveRight(len(self.TowerOne))
        return self.TowerThree



    def Hanoi2(self, n, input, buffer, output):
        if n == 1:
            output.append(input.pop())
        else:
            self.Hanoi2(n-1, input, output,buffer)
            output.append(input.pop())
            self.Hanoi2(n-1, buffer, input, output)

    def algoBetter(self):
        self.Hanoi2(len(self.TowerOne), self.TowerOne, self.TowerTwo, self.TowerThree)
        return self.TowerThree

if __name__ == '__main__':
    input = [7,6,5,4,3,2,1]
    hanoi = TowerOfHanoi(input)
    output = hanoi.algo()
    for i in range(len(output)):
        print(output.pop())
    print('\n')

    input = [7, 6, 5, 4, 3, 2, 1]
    hanoi2 = TowerOfHanoi(input)
    output = hanoi2.algoBetter()
    for i in range(len(output)):
        print(output.pop())
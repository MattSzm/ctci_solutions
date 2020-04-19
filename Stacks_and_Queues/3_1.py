class Stack3in1:
    def __init__(self):
        self.top1 = -3
        self.top2 = -2
        self.top3 = -1
        self.max_index = -1
        self.data = []

    def append(self, key, indexOfStack):
        if indexOfStack < 1 or indexOfStack > 3:
            raise AttributeError
        elif indexOfStack == 1:
            self.addCappacityIfNecessary(self.top1)
            self.top1 += 3
            self.data[self.top1] = key
        elif indexOfStack == 2:
            self.addCappacityIfNecessary(self.top2)
            self.top2 += 3
            self.data[self.top2] = key
        else:
            self.addCappacityIfNecessary(self.top3)
            self.top3 += 3
            self.data[self.top3] = key

    def is_empty(self):
        if self.max_index < 0:
            return True
        return False

    def pop(self, indexOfStack):
        if indexOfStack < 1 or indexOfStack > 3:
            raise AttributeError
        if self.is_empty():
            raise MemoryError

        if indexOfStack == 1:
            self.checkIfSingleOneIsEmpty(self.top1)
            data = self.data[self.top1]
            self.top1 -= 3
        elif indexOfStack == 2:
            self.checkIfSingleOneIsEmpty(self.top2)
            data = self.data[self.top2]
            self.top2 -= 3
        else:
            self.checkIfSingleOneIsEmpty(self.top3)
            data = self.data[self.top3]
            self.top3 -= 3

        if (self.top1 < self.max_index and self.top2 < self.max_index and
            self.top3 < self.max_index):
            self.max_index -= 3
        return data

    def addCappacityIfNecessary(self, top):
        if top + 3 > self.max_index:
            self.max_index += 3
            for i in range(3):
                self.data.append(None)

    def checkIfSingleOneIsEmpty(self, top):
        if top < 0:
            raise AttributeError

if '__main__' == __name__:
    stack = Stack3in1()
    stack.append(3,1)
    stack.append(5,3)
    stack.append(10,1)
    stack.append(12,1)
    stack.append(15,2)
    stack.append(7,3)
    print(stack.pop(1))
    print(stack.pop(1))
    print(stack.pop(2))
    print(stack.max_index)
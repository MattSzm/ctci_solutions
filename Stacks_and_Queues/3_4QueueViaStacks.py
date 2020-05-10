class Stack:
    def __init__(self):
        self.data = []

    def append(self, x):
        self.data.append(x)

    def pop(self):
        x = self.data.pop()
        return x

    def __len__(self):
        return len(self.data)


class Queue:
    def __init__(self):
        self.AStack = Stack()
        self.PStack = Stack()
        self.LastwasAppend = True

    def PushTail(self, x):
        if self.LastwasAppend:
            self.AStack.append(x)
        else:
            while(len(self.PStack)):
                memory = self.PStack.pop()
                self.AStack.append(memory)
            self.AStack.append(x)
            self.LastwasAppend = True

    def PopHead(self):
        if not (len(self.PStack) or len(self.AStack)):
            return -1
        if not self.LastwasAppend:
            x = self.PStack.pop()
        else:
            while len(self.AStack):
                memory = self.AStack.pop()
                self.PStack.append(memory)
            x = self.PStack.pop()
            self.LastwasAppend = False
        return x

class QueueV2:
    def __init__(self):
        self.NewElemnts = Stack()
        self.OldElements = Stack()

    def PushTail(self,x):
        self.NewElemnts.append(x)

    def shift(self):
        while len(self.NewElemnts):
            self.OldElements.append(self.NewElemnts.pop())

    def PopHead(self):
        if not len(self.OldElements):
            self.shift()
        if not len(self.OldElements):
            return -1
        x = self.OldElements.pop()
        return x

if __name__ == '__main__':
    queue = Queue()
    queue.PushTail(1)
    queue.PushTail(19)
    queue.PushTail(12)
    queue.PushTail(15)
    print(queue.PopHead())
    queue.PushTail(14)
    queue.PushTail(7)
    print(queue.PopHead())
    print(queue.PopHead())
    print(queue.PopHead())
    print(queue.PopHead())
    print(queue.PopHead())
    print(queue.PopHead())

    print('\n')
    queue2 = QueueV2()
    queue2.PushTail(1)
    queue2.PushTail(19)
    queue2.PushTail(12)
    queue2.PushTail(15)
    print(queue2.PopHead())
    queue2.PushTail(14)
    queue2.PushTail(7)
    print(queue2.PopHead())
    print(queue2.PopHead())
    print(queue2.PopHead())
    print(queue2.PopHead())
    print(queue2.PopHead())
    print(queue2.PopHead())
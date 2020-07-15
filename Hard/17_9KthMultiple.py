import sys

def BetterSolution(k):
    if k < 0:
        return 0

    Queue3 = []
    Queue5 = []
    Queue7 = []
    Queue3.append(1)

    for index in range(0, k):
        v1 = findPeek(Queue3)
        v2 = findPeek(Queue5)
        v3 = findPeek(Queue7)
        minValue = min(v1,v2,v3)

        if minValue == v1:
            Queue3.remove(v1)
            Queue3.append(minValue*3)
            Queue5.append(minValue*5)
        elif minValue == v2:
            Queue5.remove(v2)
            Queue5.append(minValue*5)
        elif minValue == v3:
            Queue7.remove(v3)
        Queue7.append(minValue*7)
    return minValue

def findPeek(queue):
    v = sys.maxsize
    for item in queue:
        if item < v:
            v = item
    return v

if __name__ == '__main__':
    print(Algo(23))
    print('\n')
    print(BetterSolution(23))

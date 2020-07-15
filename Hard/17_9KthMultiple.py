import sys
def WorseSolution(k):
    memo = [1]
    for i in range(0,k):
        extraMemo = []
        for m in memo:
            extraMemo.append(m*3)
            extraMemo.append(m*5)
            extraMemo.append(m*7)
        memo.extend(extraMemo)

        memo.sort()
        j=0
        for index in range(0,len(memo)):
            if memo[index-j] == memo[index-j-1]:
                memo.pop(index-j)
                j += 1
    return memo[k-1]



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
    print(BetterSolution(23))
    print(WorseSolution(23))

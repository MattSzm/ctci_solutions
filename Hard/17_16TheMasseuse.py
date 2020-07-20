
def Masseuse(input):
    memo = {}
    return Recur(input, 0, memo)


def Recur(input, currentIndex, memo):
    if memo.get(currentIndex):
        return memo[currentIndex]
    maxValue = 0
    for i in range(currentIndex, len(input)):
        currValue = Recur(input, i+2, memo) + input[currentIndex]
        maxValue = max(maxValue, currValue)
    memo[currentIndex] = maxValue
    return maxValue


def Masseuse2(input):
    memo = {}
    return Recur2(input, 0, memo)

def Recur2(input, currentIndex, memo):
    if currentIndex >= len(input):
        return 0
    if memo.get(currentIndex):
        return memo[currentIndex]

    withValue = Recur2(input, currentIndex+2, memo) + input[currentIndex]
    withoutValue = Recur2(input, currentIndex+1, memo)
    memo[currentIndex] = max(withoutValue, withValue)
    return memo[currentIndex]


if __name__ == '__main__':
    input = [30, 15, 60, 75, 45, 15, 15, 45]
    print(Masseuse(input))
    input2 = [75,105,120,75,90,135]
    print(Masseuse(input2))
    print('\n')

    print(Masseuse2(input))
    print(Masseuse2(input2))

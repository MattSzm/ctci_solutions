import math

def MissingOne(input):
    maxV = max(input)
    xor1 = 1
    xor2 = input[0]
    for ite in range(2, maxV+1):
        xor1 ^= ite

    for ite in range(1, len(input)):
        xor2 ^= input[ite]

    return xor2^xor1

def EasierOne(input):
    maxV = max(input)
    sum1 = (maxV*(maxV+1))/2

    sum2 = 0
    for el in input:
        sum2 += el

    return int(sum1-sum2)

def MissingTwo(input):
    maxV = max(input)
    sum1 = (maxV*(maxV+1))/2
    sum2 = 0
    for el in input:
        sum2 += el

    mult1 = 1
    mult2 = input[0]
    for ite in range(2, maxV+1):
        mult1 *= ite
    for ite in range(1, len(input)):
        mult2 *= input[ite]

    diff = int(sum1-sum2)
    dev = int(mult1/mult2)

    delta = diff**2-4*dev
    delta = math.sqrt(delta)

    output1 = (diff+delta)/2
    output2 = (diff-delta)/2

    return int(output1), int(output2)

if __name__ == '__main__':
    input = [2, 1, 5, 9, 4, 6, 3, 10, 12, 11, 7]
    print(MissingOne(input))
    print(EasierOne(input))

    input2 = [2, 1, 5, 9, 4, 6, 3, 10, 12, 7]
    print(MissingTwo(input2))
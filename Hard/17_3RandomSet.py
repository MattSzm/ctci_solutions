import random

def RandomSet(orginalSet, m):
    output = []
    output.extend(orginalSet[0:m])

    for index in range(m, len(orginalSet), 1):
        randomNumber = random.randint(0,index)
        if randomNumber < m:
            output[randomNumber] = orginalSet[index]

    return output

if __name__ == '__main__':
    output = RandomSet([1,2,3,4,5,6,7,8,9], 5)
    print(output)

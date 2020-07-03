import collections

def PairsWSums(inputArray, sum):
    memory = collections.Counter(inputArray)
    output = []
    for element in inputArray:
        diff = sum - element
        if memory[element] > 0 and memory[diff] > 0:
            output.append([element, diff])
            memory[element] -= 1
            memory[diff] -= 1
    return output

if __name__ == '__main__':
    input = [1,3,2,3,5,1,2,0,4,6]
    output = PairsWSums(input, 4)
    print(output)
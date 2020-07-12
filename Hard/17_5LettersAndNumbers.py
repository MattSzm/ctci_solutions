#O(n)
def algo(input):
    differences = computeDelta(input)
    indexes = returnMax(differences)
    return input[indexes['low']+1 : indexes['high']+1]


def computeDelta(input):
    output = []
    numbers = '0123456789'

    delta = 0
    for single in input:
        if single in numbers:
            delta += 1
        else:
            delta -= 1
        output.append(delta)
    return output

def returnMax(input):
    output = {'low': 0, 'high': 0}
    memory = {}
    for index in range(len(input)):
        if not memory.get(input[index]):
            memory[input[index]] = index
        else:
            diff = index - memory[input[index]]
            if diff > output['high'] - output['low']:
                output['high'] = index
                output['low'] = memory[input[index]]

    return output

if __name__ == '__main__':
    input = ['a' ,'a', 'a', 'a', '1' ,'1' ,'a' ,'1' ,'1', 'a' ,'a',
             '1', 'a', 'a', '1' ,'a' ,'a' ,'a' ,'a', 'a']

    output = algo(input)
    print(output)
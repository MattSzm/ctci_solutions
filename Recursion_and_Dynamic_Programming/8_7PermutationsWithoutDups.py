

def Permutations(string):
    if not len(string):
        return False
    memory = [string[0]]
    for index in range(1, len(string), 1):
        new_memory = []
        for item in memory:
            for i in range(len(item)+1):
                x=item[:i]+string[index]+item[i:]
                new_memory.append(x)
        memory=new_memory

    return memory


if __name__ == '__main__':
    inputS = 'abcd'
    output = Permutations(inputS)
    for i in output:
        print(i)
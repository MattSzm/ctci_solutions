import collections
def Permutations(string):
    if not len(string):
        return False
    memory = [string[0]]
    for index in range(1, len(string), 1):
        new_memory = []
        for item in memory:
            for i in range(len(item)+1):
                x=item[:i]+string[index]+item[i:]
                if not x in new_memory:
                    new_memory.append(x)
        memory=new_memory

    return memory

def PermutationsBetter(string:str )->list:
    memory = collections.Counter(string)
    output = []
    PerBetterRecursion('', len(string), memory, output)
    return output

def PerBetterRecursion(prefix:str, rest:int, memory, output):
    if rest == 0:
        output.append(prefix)
        return
    for key in memory:
        if memory[key] > 0:
            memory[key] -= 1
            PerBetterRecursion(prefix+key, rest-1, memory, output)
            memory[key] += 1





if __name__ == '__main__':
    inputS = 'abb'
    output = Permutations(inputS)
    for i in output:
        print(i)
    print('\n')
    
    inputS = 'abb'
    output = PermutationsBetter(inputS)
    for i in output:
        print(i)
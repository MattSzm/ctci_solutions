

def Permutations(string: str)->list:
    output = []
    PermutationsRecursive(string, '', output)
    return output

def PermutationsRecursive(rest, prefix, output):
    if len(rest) == 0:
        output.append(prefix)
        return
    for i in range(len(rest)):
        new_rest= rest[:i] + rest[i+1:]
        PermutationsRecursive(new_rest, prefix+rest[i], output)


if __name__ == '__main__':
    inputS = 'abcd'
    output = Permutations(inputS)
    for i in output:
        print(i)
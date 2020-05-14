import copy
def subSet(input, i, j, previousSub, memory):
    for iter in range(i, j):
        x = copy.copy(previousSub)
        x.append(input[iter])
        memory.append(x)
        subSet(input, iter+1, j, x, memory)

def subMain(input):
    memory = []
    subSet(input,0, len(input),[],memory)
    return memory


if __name__ == '__main__':
    input = [1,2,3,4]
    output = subMain(input)
    print(output)
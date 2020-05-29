def Coins(n,previousCoin, memory):
    if memory.get(n):
        if memory[n].get(previousCoin):
            return memory[n][previousCoin]
    if n<0:
        return 0
    if n == 0:
        return 1
    output = 0
    if previousCoin >= 25:
        output += Coins(n-25, 25, memory)
    if previousCoin >= 10:
        output += Coins(n-10, 10, memory)
    if previousCoin >= 5:
        output += Coins(n-5, 5, memory)
    if previousCoin >= 1:
        output += Coins(n-1, 1, memory)

    if memory.get(n):
        memory[n][previousCoin] = output
    else:
        memory[n] = {previousCoin: output}
    return output

def CoinsWrapper(n):
    memory = {}
    return Coins(n,n, memory)

if __name__ == '__main__':
    print(CoinsWrapper(4356))
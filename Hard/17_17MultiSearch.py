def multiSearch(smalls, big):
    memo = {}
    for item in smalls:
        results = findIndexes(item, big)
        memo[item] = results
    return memo

def findIndexes(item, big):
    output = []
    for index in range(0, len(big)-len(item)+1,1):
        if item == big[index:index+len(item)]:
            output.append(index)
    return output



if __name__ == '__main__':
    T = ["is", "ppi", "hi", "sis", "i", "ssippi"]
    b = "mississippi"
    output = multiSearch(T,b)
    print(output)
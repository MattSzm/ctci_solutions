def WordRed(dictionary):
    maxLength = 0
    memo = {}
    for el in dictionary:
        maxLength = max(maxLength, len(el))
        if memo.get(len(el)):
            memo[len(el)].append(el)
        else:
            memo[len(el)] = [el]

    bestResultOutput = []
    bestResultSize = 0
    for currLen in range(maxLength, 0, -1):
        if currLen**2 <= bestResultSize:
            break

        if memo.get(currLen):
            for _ in memo[currLen]:
                index = 1
                while index < len(memo[currLen]):
                    output, size = findWords(memo, currLen)
                    if size > bestResultSize:
                        bestResultSize = size
                        bestResultOutput = output
                    memo[currLen][index-1], memo[currLen][index] =  memo[currLen][index],memo[currLen][index-1]
                    index += 1
    return bestResultOutput, bestResultSize


def findWords(memo, currLength,):
    for length in range(currLength, 0, -1):
        if memo.get(length):
            pickedWords = memo[currLength][:length]

            flag = False
            for index in range(0, length, 1):
                word = ''
                for singleWord in pickedWords:
                    word += singleWord[index]

                if not word in memo[length]:
                    flag = True
                    break

            if not flag:
                return pickedWords, currLength*length
    return [], 0


if __name__ == '__main__':
    input = ['dip','dog','map','hard','amp','house','gap','much','surrender','gryps,',
             'upa','ipa','never','dagi','omap','so','gppa','cat','maybe','many']
    output, size = WordRed(input)
    print(size)
    for word in output:
        print(word)
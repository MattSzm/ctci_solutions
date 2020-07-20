def LongestWord(input:list)->str:
    input.sort(key=lambda x: len(x), reverse=True)
    shortestLength = len(input[len(input)-1])
    output = ''

    for index in range(len(input)):
        redFlag = False
        currentWord = input[index]

        cWIndex = 0
        while cWIndex < len(currentWord):
            for currentLength in range(len(currentWord)-1, shortestLength-1, -1):
                if currentWord[cWIndex:cWIndex+currentLength] in input:
                    output += currentWord[cWIndex:cWIndex+currentLength]
                    cWIndex += currentLength
                    break
            else:
                cWIndex = len(currentWord)
                redFlag = True
        if not redFlag and len(currentWord) == len(output):
            return currentWord
    return '-1'

def LongestWordV2(input:list)->str:
    input.sort(key=lambda x: len(x), reverse=True)

    for index in range(len(input)):
        currentWord = input[index]
        memo = {'found': False}
        result = Recursion(input, currentWord, len(currentWord)-1, memo)
        if result:
            return currentWord
    return '-1'


def Recursion(input, currentWord, indexPrefix, memo):
    if currentWord[0:indexPrefix] == '':
        memo['found'] = True
        return
    if currentWord[0:indexPrefix] in input:
        newCurrentWord = currentWord[indexPrefix:]
        Recursion(input, newCurrentWord, len(newCurrentWord), memo)
    if indexPrefix-1 == 0:
        return
    if not memo['found']:
        Recursion(input, currentWord, indexPrefix-1, memo)
    return memo['found']




if __name__ == '__main__':
    input = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'dogwalker']
    output = LongestWord(input)
    print(output)

    input2 = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'dogwalker']
    output = LongestWordV2(input2)
    print(output)
#simplified question

def Algo(string:str, dict:list)->str:
    maxLength = 0
    output = ''

    for word in dict:
        if len(word) > maxLength:
            maxLength = len(word)

    wasRecognized = True
    index = 0
    while index < len(string):
        for i in range(maxLength):
            if string[index:index+i+1] in dict:
                if not wasRecognized:
                    output += ' '
                output += string[index:index+i+1] + ' '
                index += i +1
                wasRecognized = True
                break
        else:
            output += string[index]
            wasRecognized = False
            index += 1
    return output

if __name__ == '__main__':
    input = 'jesslookedjustliketimherbrother'
    dict = ['looked', 'just', 'like', 'her', 'brother', 'a','dog','cat','dad','his','family',
            'house']
    print(Algo(input,dict))
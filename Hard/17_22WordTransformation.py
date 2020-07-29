def word_transformation(previousString:str, outputString:str, dict:list):
    length = len(previousString)
    memo = [False]*length
    for index in range(length):
        if previousString[index] != outputString[index]:
            memo[index] = True

    output =  recur(previousString, outputString, dict, memo, [])
    if output:
        output.append(previousString)
    return output

def recur(previousString:str, outputString:str, dict:list, memo:list, output:list):
    if not True in memo:
        return True
    length = len(previousString)
    for index in range(length):
        if memo[index]:
            current = (previousString[:index] + outputString[index]
                       + previousString[index + 1:])
            if current in dict:
                memo[index] = False
                status = recur(current, outputString, dict, memo, output)
                memo[index] = True
                if status:
                    if status == True:
                        status = []
                    status.append(current)
                    return status
    return False


def word_transformation2(previousString:str, outputString:str, dict:list):
    output =  recur2([previousString], outputString, dict)
    return output


def recur2(previousStrings:list, outputString:str, dict:list):
    output = []
    length = len(outputString)
    for prev in previousStrings:
        if prev == outputString:
            return prev
        for index in range(length):
            if prev[index] != outputString[index]:
                current = (prev[:index] + outputString[index]
                           + prev[index + 1:])
                if current in dict:
                    output.append(current)
    if len(output) == 0:
        return False
    return recur2(output, outputString, dict)


if __name__ == '__main__':
    one = 'DAMP'
    two = 'LIKE'
    memo = ['DAME','CAT','LIKP','DAMP','DAD','HOUSE','LIMP','LIKE','DUCK','LIVE','MAKE',
            'LIME','UBER','LIDP','LEMP','LIMA','LEMP','LAMP']
    output = word_transformation(one, two, memo)
    print(output)

    one = 'camp'
    two = 'dbub'
    memo = ['dbmb', 'clar', 'camp', 'camb', 'deny', 'dubm', 'dumby', 'cbmb', 'diggi', 'dbmb', 'dbub']
    output = word_transformation(one, two, memo)
    print(output)

    one = 'camp'
    two = 'dbub'
    memo = ['dbmb', 'clar', 'camp', 'camb', 'deny', 'dubm', 'dumby', 'cbmb', 'diggi', 'dbmb']
    output = word_transformation(one, two, memo)
    print(output)

    one = 'DAMP'
    two = 'LIKE'
    memo = ['DAME', 'CAT', 'LIKP', 'DAMP', 'DAD', 'HOUSE', 'LIMP', 'LIKE', 'DUCK', 'LIVE', 'MAKE',
            'LIME', 'UBER', 'LIDP', 'LEMP', 'LIMA', 'LEMP', 'LAMP']
    output = word_transformation2(one, two, memo)
    print(output)

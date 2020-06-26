
def PatternMatching(input:str, pattern:str)->bool:
    length = len(input)
    aCount = 0
    bCount = 0
    for i in pattern:
        if i == 'A':
            aCount += 1
        elif i == 'B':
            bCount += 1
        else:
            return False

    for aLength in range(0, length):
        rest = length - aLength*aCount
        if bCount != 0:
            bLength = int(rest/bCount)
        else:
            bLength = 0

        if bLength == 0 and bCount != 0:
            return False
        elif bLength == 0 or bLength == rest/bCount:
            currIndex = 0
            aCurr = None
            bCurr = None
            for value in pattern:
                if value == 'A':
                    if not aCurr:
                        aCurr = input[currIndex:currIndex+aLength]
                    else:
                        if input[currIndex:currIndex+aLength] != aCurr:
                            break
                    currIndex += aLength
                elif value == 'B':
                    if not bCurr:
                        bCurr = input[currIndex:currIndex+bLength]
                    else:

                        if input[currIndex:currIndex+bLength] != bCurr:
                            break
                    currIndex += bLength
            else:
                if currIndex == length:
                    return True
    return False


if __name__ == '__main__':
    output = PatternMatching('catcatgocatgocat','AABABA')
    print(output)

def soSimpleSoGood(shorter:int, longer:int, k:int)->list:
    output = []
    for leftSide in range(0,k+1):
        rightSide = k-leftSide
        output.append(leftSide*shorter + rightSide*longer)

    return output

if __name__ == '__main__':
    output = soSimpleSoGood(3,5,10)
    print(output)
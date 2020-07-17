
def Algo(input:list)->int:
    majority = None
    count = 0

    for element in input:
        if count == 0:
            majority = element

        if majority == element:
            count += 1
        else:
            count -= 1

    return majority if Check(input,majority) else -1


def Check(input:list, majority:int)->bool:
    count = 0
    for i in input:
        if i == majority:
            count += 1

    return count > int(len(input)/2)

if __name__ == '__main__':
    print(Algo([3, 1, 7, 1, 3, 7, 3, 7, 1, 7, 7]))
    print(Algo([1, 2, 5, 9, 5, 9, 5, 5, 5]))
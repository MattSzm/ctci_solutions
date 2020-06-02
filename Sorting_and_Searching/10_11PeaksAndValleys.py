
def PaV(array:list)->list:
    sorted_ = sorted(array)
    secodIndex = 0
    for index in range(int(len(sorted_)/2)):
        array[secodIndex] = sorted_[len(sorted_)-index-1]
        array[secodIndex+1] = sorted_[index]
        secodIndex += 2

    return array

def PavBetter(array:list)->list:
    for index in range(1, len(array), 2):
        biggestIndex = maxIndex(array, index-1, index, index+1)
        if biggestIndex != index:
            array[biggestIndex], array[index] = array[index], array[biggestIndex]

    return array


def maxIndex(array, left, main, right):
    max = left
    if array[main] > array[left]:
        max = main
    if not right >= len(array):
        if array[right] > array[max]:
            max = right

    return max

if __name__ == '__main__':
    input = [4,6,5,9,8,46,9,2,1,1,35,6]
    output = PaV(input)
    print(output)

    input = [4, 6, 5, 9, 8, 46, 9, 2, 1, 1, 35, 6]
    output = PavBetter(input)
    print(output)
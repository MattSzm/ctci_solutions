def SmallestKBruteForce(array:list, k:int)->list:
    if k>len(array) or k <= 0:
        return -1

    array.sort()
    output = []
    counter = 0

    for index in range(len(array)):
        if array[index] != array[index-1]:
            output.append(array[index])
            counter += 1
        if k == counter:
            break

    return output

#if integers
def SmallestK(array:list, k:int)->list:
    if k > len(array) or k <= 0:
        return -1
    maxValue = max(*array)
    memo = [0 for _ in range(maxValue+1)]

    for value in array:
        memo[value] += 1

    output = []
    kc = 0
    for index in range(len(memo)):
        if memo[index] > 0:
            output.append(index)
            kc += 1
        if kc == k:
            return output

#if unique
def heapify(heap, index):
    size = len(heap)
    left = index*2+1
    right = index*2+2

    maxIndex = index
    if left < size and heap[left]>heap[maxIndex]:
        maxIndex = left
    if right < size and heap[right]>heap[maxIndex]:
        maxIndex = right

    if maxIndex != index:
        heap[maxIndex],heap[index] = heap[index],heap[maxIndex]
        heapify(heap, maxIndex)



def SmallestKHeap(array:list, k:int)->list:
    if k > len(array) or k <= 0:
        return -1
    heap = []

    i = 0
    while i < k:
        heap.insert(0, array[i])
        heapify(heap, 0)
        i += 1

    while i < len(array):
        if array[i] < heap[0]:
            heap.append(array[i])
            heap[0], heap[k] = heap[k],heap[0]
            heap.pop()
            heapify(heap,0)
        i += 1

    output = [0 for _ in range(k)]
    for i in range(k-1,-1,-1):
        output[i] = heap.pop(0)
        heapify(heap,0)
    return output



if __name__ == '__main__':
    input = [8, 4, 3, 5, 6, 0, 13, 4, 65, 1, 3, 5, 1, 3]
    print(SmallestKBruteForce(input, 4))
    input = [8, 4, 3, 5, 6, 0, 13, 4, 65, 1, 3, 5, 1, 3]
    print(SmallestK(input,4))
    input = [8, 4, 3, 5, 6, 0, 13, 65, 1]
    print(SmallestKHeap(input,4))
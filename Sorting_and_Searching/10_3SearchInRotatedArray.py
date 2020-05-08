def search(arr, left, right, x):
    mid = int((left+right)/2)
    if arr[mid] == x:
        return mid

    if left > right:
        return -1

    if arr[left] < arr[mid]:
        if x >= arr[left] and x < arr[mid]:
            return search(arr,left, mid-1, x)
        else:
            return search(arr, mid+1, right)
    elif arr[mid] < arr[left]:
        if x > arr[mid] and x <= arr[right]:
            return search(arr, mid+1, right,x)
        else:
            return search(arr, left, mid-1,x)
    elif arr[left] == arr[mid]:
        if arr[mid] != arr[left]:
            return search(arr,mid+1,right,x)
        else:
            result = search(arr, left, mid-1, x)
            if result == -1:
                return search(arr, mid+1,right, x)
            else:
                return result
    return -1

if __name__ == '__main__':
    input = [15, 16, 19, 20, 25, 1, 3, 4, 5, 7, 10, 14]
    output = search(input, 0 ,len(input)-1, 5)
    print(output)
def swap(x:int)->int:
    lenght = 0
    copy = x
    while copy >= 1:
        lenght += 1
        copy /= 2

    maskEven = ''
    for i in range(int(lenght/2)+1):
        maskEven += '10'
    maskEven = int(maskEven,2)

    maskOdd = ''
    for i in range(int(lenght/2)+1):
        maskOdd += '01'
    maskOdd = int(maskOdd,2)
    return ((maskEven&x)>>1)|((maskOdd&x)<<1)

if __name__ == '__main__':
    a = 45
    print(swap(a))
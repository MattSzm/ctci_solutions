def Parens(n:int)->list:
    if n <= 0:
        return False
    output = []
    ParensRecur(n-1,n,output,'(')
    return output

def ParensRecur(left:int, right:int, output:list, prefix:str):
    if left == 0 and right == 0:
        output.append(prefix)
        return
    if left != 0:
        ParensRecur(left-1,right, output, prefix+'(')
    if right > left:
        ParensRecur(left, right-1, output, prefix+')')

if __name__ == '__main__':
    output = Parens(3)
    print(output)
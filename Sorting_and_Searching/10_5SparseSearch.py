import unittest

def SparseSearch(inputArray, x):
    l = 0
    max_index = len(inputArray)-1
    r = max_index
    while r>=l:
        m=int((r+l)/2)
        if inputArray[m] == '':
            Loffset=0
            Roffset=0

            while m-Loffset>0 and m+Roffset<max_index:
                Roffset += 1
                Loffset += 1
                if inputArray[m+Roffset]!=''or inputArray[m-Loffset]!='':
                    break
            if inputArray[m+Roffset]!='':
                if comp(inputArray,x,m+Roffset):
                    return m+Roffset
            if inputArray[m-Loffset]!='':
                if comp(inputArray,x,m-Loffset):
                    return m-Loffset

            if bigger(inputArray,x,m+Roffset):
                l=m+Roffset+1
            else:
                r=m-Loffset-1
        else:
            if comp(inputArray,x,m):
                return m
            elif bigger(inputArray,x,m):
                l = m+1
            else:
                r=m-1
    return -1

def comp(inputArray,x, index):
    if index>=len(inputArray) or index <0:
        return False
    for i in range(len(x)):
        if x[i] != inputArray[index][i]:
            return False
    return True

def bigger(inputArray,x, index):
    if index>=len(inputArray) or index < 0:
        return False
    for i in range(len(x)):
        if x[i] != inputArray[index][i]:
            if x[i] > inputArray[index][i]:
                return True
            else:
                return False

class tests(unittest.TestCase):
    data=[
        ('ball',['at','','','','ball','','','car','','','dad','',''],4)
    ]

    def test_True(self):
        for [x,input,expected] in self.data:
            output = SparseSearch(input,x)
            self.assertEqual(output,expected)

if __name__=='__main__':
    unittest.main()

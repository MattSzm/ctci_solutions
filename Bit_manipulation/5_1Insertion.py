import unittest

def Insertion(M, N, i, j):
    for k in range(j-i+1):
        value = get(M, k)
        N = update(N, value, i+k)
    return N

def get(M, index):
    if int(M,2)&(1<<index):
        return 1
    return 0

def update(N, value, index):
    N = int(N,2)&(~(1<<index))
    N = N|(value<<index)
    return bin(N)

def InsertionBetter(M, N, i, j):
    allones = ~0
    downmask = allones<<j+1
    highmask = (1<<i)-1
    mask = highmask|downmask
    N = int(N,2)&mask
    M = M << i
    return bin(N|M)

class test(unittest.TestCase):
    M = '10011'
    N = '10000000000'
    i=2
    j=6

    def insertionTest(self):
        expected = '10001001100'
        result = Insertion(self.M,self.N,self.i,self.j)
        self.assertEqual(expected,result)

    def insertionBetterTest(self):
        expected = '10001001100'
        result = InsertionBetter(self.M,self.N,self.i,self.j)
        self.assertEqual(expected,result)

if __name__ == '__main__':
    unittest.main()

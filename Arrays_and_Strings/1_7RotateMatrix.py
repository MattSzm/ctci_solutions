import unittest

def Rotate(matrix):
    n = len(matrix)
    new_matrix = [[0 for _ in range(n)] for __ in range(n)]
    for i in range(n):
        for j in range(n):
            new_matrix[n-j-1][i]=matrix[i][j]
    return new_matrix

def RotateBetter(matrix):
    n=len(matrix)
    nh=int(n/2)

    for i in range(nh):
        for index in range(n-2*i-1):
            Fmemory = matrix[i][i + index]
            Smemory = matrix[n - index - i - 1][i]
            matrix[n - index - i - 1][i] = Fmemory
            Fmemory = matrix[n - i - 1][n - index - i - 1]
            matrix[n - i - 1][n - index - i - 1] = Smemory
            Smemory = matrix[i + index][n - i - 1]
            matrix[i + index][n - i - 1] = Fmemory
            matrix[i][i + index] = Smemory

    return matrix

class tests(unittest.TestCase):
    data = [(
        [[6, 2, 7],
         [1, 3, 6],
         [5, 5, 2]],
        [[7, 6, 2],
         [2, 3, 5],
         [6, 1, 5]]
    ),
        ([[2, 6, 7, 8],
         [4, 5, 6, 6],
         [3, 2, 2, 1],
         [3, 4, 1, 5]],
        [[8, 6, 1, 5],
         [7, 6, 2, 1],
         [6, 5, 2, 4],
         [2, 4, 3, 3]])
    ]


    def test_Rotate(self):
        for [input, expected] in self.data:
            output = Rotate(input)
            self.assertListEqual(output, expected)

    def test_RotateBetter(self):
        for [input, expected] in self.data:
            output = RotateBetter(input)
            self.assertListEqual(expected,output)

if __name__ == '__main__':
    unittest.main()

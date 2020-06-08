import unittest

def TicTac(input):
    for i in range(0,3):
        memoOne = input[i][0]
        memoTwo = input[0][i]
        for j in range(1,3):
            if memoOne != input[i][j]:
                break
            elif j == 2:
                return True

        for j in range(1,3):
            if memoTwo != input[j][i]:
                break
            elif j == 2:
                return True

    if (input[0][0]==input[1][1]==input[2][2] or
        input[0][2]==input[1][1]==input[2][0]):
        return True
    return False

class tests(unittest.TestCase):
    a = [['x','o','empty'],
         ['x','x','o'],
         ['o','o','x']]
    b = [['o','x','o'],
         ['x','o','x'],
         ['x','o','x']]

    def test_True(self):
        output = TicTac(self.a)
        self.assertTrue(output)

    def test_False(self):
        output= TicTac(self.b)
        self.assertFalse(output)

if __name__ == '__main__':
    unittest.main()
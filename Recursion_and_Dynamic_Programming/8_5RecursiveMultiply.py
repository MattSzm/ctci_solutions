import unittest

#SLOWWWWWWWWWW
def Multiply(a,b):
    if b>0:
        return a + Multiply(a, b-1)
    else:
        return 0

def MultiMain(a,b):
    if a==0 or b==0:
        return 0
    elif a>b:
        return Multiply(a,b)
    else:
        return Multiply(b,a)

class tests(unittest.TestCase):
    data = [
        (5,4,20),
        (3,7,21),
        (0,5,0),
        (23,41,943)
    ]

    def test(self):
        for [a,b,expected] in self.data:
            output = MultiMain(a,b)
            self.assertEqual(output,expected)

if __name__ == '__main__':
    unittest.main()
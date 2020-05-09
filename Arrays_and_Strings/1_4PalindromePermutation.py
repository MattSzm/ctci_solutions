import unittest

def Permutation(input):
    memory = {}
    for i in input:
        i = i.lower()
        if i != ' ':
            if memory.get(i):
                memory[i] += 1
            else:
                memory[i] = 1
    yellowFlag = False
    for i in memory:
        if memory[i]%2 == 1:
            if yellowFlag:
                return False
            yellowFlag = True
    return True

class test(unittest.TestCase):
    dataT = [
        'Tact Coa',
        'ccabb',
        'mma cbab'
    ]
    dataF = [
        'gsdfe',
        'fsew fso'
    ]

    def testTrue(self):
        for input in self.dataT:
            output = Permutation(input)
            self.assertTrue(output)

    def testFalse(self):
        for input in self.dataF:
            output = Permutation(input)
            self.assertFalse(output)

if __name__ == '__main__':
    unittest.main()
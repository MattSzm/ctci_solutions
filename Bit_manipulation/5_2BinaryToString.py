import unittest

def BinaryToSting(doubleV):
    if doubleV < 0 or doubleV > 0:
        return 'ERROR'
    output = '.'
    value = 0.5
    while doubleV > 0:
        if len(output) > 32:
            return 'ERROR'
        if doubleV>=value:
            doubleV-=value
            output += '1'
        else:
            output += '0'
        value /= 2
    return output

class Tests(unittest.TestCase):
    dataT = [(0.5,'.1'),
             (0.75,'.11'),
             (0.5625,'.1001')
             ]
    dataF = [
        0.101, 0.46599446591, 1.312
    ]

    def TestTrue(self):
        for [doubleV, result] in self.dataT:
            output = BinaryToSting(doubleV)
            self.assertEqual(result,output)

    def TestFalse(self):
        for doubleV in self.dataF:
            output = BinaryToSting(doubleV)
            self.assertEqual(output,'ERROR')

if __name__ == '__main__':
    unittest.main()

import unittest

def permutation(firstString, secondString):
    len1 = len(firstString)
    len2 = len(secondString)

    if len1 != len2 or (len1 == 0 and len2 == 0):
        return False
    memory = {}
    for item in firstString:
        if memory.get(item):
            memory[item] += 1
        else:
            memory[item] = 1
    for item in secondString:
        k = memory.get(item)
        if not k:
            return False
        elif k == 1:
            del memory[item]
        else:
            memory[item] -= 1
    return True



class Test(unittest.TestCase):
    dataT = (
        ('abb', 'bab'),
        ('38 fse', ' es3f8')
    )
    dataF = (
        ('bad', 'abb'),
        ('32 4s', 'fsd 2')
    )

    def test(self):
        for test_strings in self.dataT:
            result = permutation(*test_strings)
            self.assertTrue(result)
        for test_strings in self.dataF:
            result = permutation(*test_strings)
            self.assertFalse(result)

if '__main__' == __name__:
    unittest.main()
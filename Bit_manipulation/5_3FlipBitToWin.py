import unittest

def flipBIt(number):
    if (~number == 0):
        return False
    current_value = 0
    previous_value = 0
    max_value = 0
    while number != 0:
        if number&1 != 0:
            current_value += 1
        else:
        #number&1 == 0
            if number&2 == 0:
                previous_value = 0
            else:
                previous_value = current_value
            current_value = 0
        max_value = max(max_value, previous_value+current_value+1)
        number >>= 1

class tests(unittest.TestCase):
    dataT = [
        (1775,8),
        (619,4)
    ]
    dataF= [127]

    def workingTest(self):
        for [input, expected] in self.dataF:
            output = flipBIt(input)
            self.assertEqual(output,expected)

    def notWorkingTest(self):
        for input in self.dataF:
            output = flipBIt(input)
            self.assertFalse(output)

if __name__ == '__main__':
    unittest.main()
import unittest

def Compression(string):
    if len(string) == 0:
        return -1
    output = ''
    previous = None
    count = 0
    for current in string:
        if previous:
            if previous == current:
                count+=1
            else:
                output += previous
                output += str(count)
                previous = current
                count = 1
        else:
            previous = current
            count = 1
    output += previous
    output += str(count)
    if len(output) < len(string):
        return output
    return string


class tests (unittest.TestCase):
    data =[
        ('aabcccccaaa','a2b1c5a3'),
        ('',-1),
        ('abcdef','abcdef')
    ]

    def test_working(self):
        for [input,expected] in self.data:
            output = Compression(input)
            self.assertEqual(output, expected)

if __name__ == '__main__':
    unittest.main()

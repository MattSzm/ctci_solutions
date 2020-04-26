import unittest

def URLify(str):
    output = ''
    str = list(str)
    for ch in str:
        if ch == ' ':
            output += '%20'
        else:
            output += ch
    return output

def URLify_wo_memory(str, lenght):
    new_length = len(str)
    for i in reversed(range(lenght)):
        if str[i] == ' ':
            str[new_length-3 : new_length] = '%20'
            new_length -= 3
        else:
            str[new_length-1] = str[i]
            new_length -= 1
    return str

class Test(unittest.TestCase):
    data = [
        (list('much ado about nothing      '), 22,
         list('much%20ado%20about%20nothing')),
        (list('Mr John Smith    '), 13, list('Mr%20John%20Smith'))
    ]
    data_v2 = [
        ('Mr John Smith', 'Mr%20John%20Smith')
    ]
    def test_utlify_wo_memory(self):
        for [test_string, expected] in self.data_v2:
            output = URLify_wo_memory(test_string)
            self.assertEqual(expected, output)

    def test_utlify_wo_memory(self):
        for [test_string, lenght, expected] in self.data:
            output = URLify_wo_memory(test_string, lenght)
            self.assertEqual(expected, output)


if __name__ == '__main__':
    unittest.main()

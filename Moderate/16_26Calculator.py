import unittest

def calcualtor(input):
    operators = ['/*', '+-']
    memory = []
    previousIndex = 0
    for index in range(len(input)):
        if index == len(input) - 1:
            memory.append(float(input[previousIndex:len(input)]))
        elif input[index] in operators[0] or input[index] in operators[1]:
            memory.append(float(input[previousIndex:index]))
            memory.append(input[index])
            previousIndex = index + 1

    for i in range(2):
        index = 0
        currOperators = operators[i]
        while index != len(memory):
            if str(memory[index]) in currOperators:
                result = compute(memory[index-1], memory[index+1], memory[index])
                memory[index-1] = result
                del memory[index:index+2]
            else:
                index += 1

    return memory[0]


def compute(firstPart, secondPart, operator):
    if operator == '+':
        return float(firstPart) + float(secondPart)
    elif operator == '-':
        return float(firstPart) - float(secondPart)
    elif operator == '*':
        return float(firstPart) * float(secondPart)
    else:
        return float(firstPart) / float(secondPart)

class tests(unittest.TestCase):
    data = (
        ['2*3+5/6*3+15', 23.5],
        ['4*2+1/2+3-4/1', 7.5]
    )

    def test(self):
        for [input, result] in self.data:
            output = calcualtor(input)
            self.assertEqual(output, result)

if __name__ == '__main__':
    unittest.main()
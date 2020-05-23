import unittest

def BuildOrder(projects, depend):
    memory = {}
    memoryOfUse = {}
    for i in projects:
        memory[i]=[]
        memoryOfUse[i]=0
    for i in depend:
        memory[i[0]].append(i[1])
        memoryOfUse[i[1]] += 1

    Queue = []
    for i in memoryOfUse:
        if memoryOfUse[i] == 0:
            Queue.append(i)
    output = []
    while len(Queue) != 0:
        x = Queue.pop(0)
        for i in memory[x]:
            memoryOfUse[i] -= 1
            if memoryOfUse[i] == 0:
                Queue.append(i)
        output.append(x)

    if len(output) == len(projects):
        return output
    return False


class tests(unittest.TestCase):
    projects = [1, 2, 3, 4,6]
    dependencies = [[1, 3], [2, 1], [4, 3]]
    expected = [2,4,6,1,3]

    projects2 = ['a', 'b', 'c', 'd', 'e', 'f']
    dependencies2 = [['a','d'],['f','b'],['b','d'],['f','a'],['d','c']]
    expected2 = ['e','f','b','a','d','c']


    projectsError = [1, 2, 3]
    dependenciesError = [[1, 3], [2, 3], [3, 1]]

    def test_working(self):
        output = BuildOrder(self.projects, self.dependencies)
        self.assertListEqual(output, self.expected)

        output = BuildOrder(self.projects2, self.dependencies2)
        self.assertListEqual(self.expected2,output)

    def test_false(self):
        output = BuildOrder(self.projectsError, self.dependenciesError)
        self.assertFalse(output)

if __name__ == '__main__':
    unittest.main()
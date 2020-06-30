
class Node:
    def __init__(self, value, isWord=False):
        self.value = value
        self.isWord = isWord
        self.children = []

class Tree:
    def __init__(self):
        self.root = Node('')
        self.memory = {'1':[], '2':['a','b','c'],
                       '3':['d','e','f'],'4':['g','h','i'],
                       '5':['j','k','l'],'6':['m','n','o'],
                       '7':['p','q','r','s'],'8':['t','u','v'],
                       '9':['w','x','y','z'],'0':[]}

    def findWords(self, input, output, previousNode, prefix=''):
        if len(input) == 0 and previousNode.isWord:
            output.append(prefix)
            return
        elif len(input) == 0:
            return
        number = input.pop(0)
        allLetters = self.memory[number]
        for child in previousNode.children:
            if child.value in allLetters:
                self.findWords(input, output, child, prefix+child.value)
        input.insert(0, number)

    def T9(self, input):
        realInput = []
        for i in input:
            realInput.append(i)
        output = []
        self.findWords(realInput, output, self.root)
        return output



if __name__ == '__main__':
    tree = Tree()
    t1 = Node('t')
    u1 = Node('u')
    z1 = Node('z')
    o1 = Node('o')
    tree.root.children = [t1,u1,z1,o1]
    r2 = Node('r')
    j2 = Node('j')
    t1.children = [r2,j2]
    s2 = Node('s')
    w2 = Node('w')
    u1.children = [s2, w2]
    e3 = Node('e')
    d3 = Node('d')
    r2.children = [e3,d3]
    e4 = Node('e')
    s2.children = [e4]
    e5 = Node('e',True)
    o5 = Node('o',True)
    e3.children = [e5,o5]
    d6 = Node('d',True)
    w6 = Node('w',True)
    e4.children = [d6,w6]
    t7 = Node('t',True)
    d6.children = [t7]

    output = tree.T9('8733')
    print(output)
#Bad one!

class Node:
    def __init__(self, x, left=None, right=None):
        self.x=x
        self.left=left
        self.right=right

def Sequences(root):
    if not root:
        return []
    leftSide = Sequences(root.left)
    rightSide = Sequences(root.right)
    output = []
    prefix = [root.x]

    for leftItem in leftSide:
        for rightItem in rightSide:
            waved = []
            WaveLists(leftItem, rightItem, waved, prefix)
            output.append(waved)

    if len(output)==0:
        return [prefix]
    return output

def WaveLists(left, right, output, prefix):
    if len(left) == 0 or len(right) == 0:
        result = prefix + left + right
        output.append(result)
        return

    headLeft = left.pop(0)
    prefix.append(headLeft)
    WaveLists(left,right, output,prefix)
    prefix.pop(len(prefix)-1)
    left.insert(0, headLeft)

    headRight = right.pop(0)
    prefix.append(headRight)
    WaveLists(left,right, output,prefix)
    prefix.pop(len(prefix)-1)
    right.insert(0,headRight)




if __name__ == '__main__':
    a = Node(2)
    b = Node(4)
    c = Node(3, a, b)
    d = Node(7)
    e = Node(12)
    f = Node(9, d, e)
    root = Node(5, c, f)

    output = Sequences(root)
    print(output)
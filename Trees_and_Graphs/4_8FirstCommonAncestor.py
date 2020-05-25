class Node:
    def __init__(self,x ,left=None, right=None):
        self.x=x
        self.left=left
        self.right=right

    def __str__(self):
        return '0'

def Ancestor(root, firstNode, secondNode):
    if not root:
        return False
    thisNode = False
    if root == firstNode or root == secondNode:
        thisNode = True
    leftHalf = Ancestor(root.left, firstNode, secondNode)
    rightHalf = Ancestor(root.right, firstNode, secondNode)

    if str(leftHalf) == 'returnPrevious' or str(rightHalf) == 'returnPrevious':
        return root

    if type(leftHalf) != bool:
        return leftHalf
    elif type(rightHalf) != bool:
        return rightHalf

    if leftHalf and rightHalf:
        return root
    elif (leftHalf and thisNode) or (rightHalf and thisNode):
        return 'returnPrevious'

    if thisNode or leftHalf or rightHalf:
        return True
    return False

def AncestorMain(root, firstNode, secondNode):
    output = Ancestor(root, firstNode, secondNode)
    if output == True:
        return False
    return output


if __name__ == '__main__':
    a = Node('a')
    b = Node('b')
    c = Node('c',a,b)
    d = Node('d')
    e = Node('e')
    f = Node('f',d,e)
    g = Node('g')
    h = Node('h',f,g)
    root = Node('root',c,h)
    i = Node('i')

    output = AncestorMain(root, d, g)
    print(output.x)
    output = AncestorMain(root,d,i)
    print(output)
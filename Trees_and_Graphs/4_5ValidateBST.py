import unittest

class Node:
    def __init__(self,x, left=None, right=None):
        self.x = x
        self.left = left
        self.right = right

def Validate(root):
    if not root:
        return False
    return CheckBalance(root)


def CheckBalance(root, lastLeftParent=None, lastRightParent=None):
    if not root.left:
        leftHalf=True
    elif root.left.x <= root.x:
        if lastLeftParent:
            if root.left.x > lastLeftParent.x:
                leftHalf = CheckBalance(root.left, lastLeftParent, root)
            else:
                leftHalf=False
        else:
            leftHalf = CheckBalance(root.left, lastLeftParent, root)
    else:
        leftHalf=False

    if not root.right:
        rightHalf=True
    elif root.right.x > root.x:
        if lastRightParent:
            if root.right.x < lastRightParent.x:
                rightHalf = CheckBalance(root.right, root, lastRightParent)
            else:
                rightHalf=False
        else:
            rightHalf = CheckBalance(root.right, root, lastRightParent)
    else:
        rightHalf=False
    return leftHalf&rightHalf

class tests(unittest.TestCase):
    a=Node(1)
    c=Node(3)
    d=Node(2,left=a,right=c)
    e=Node(3)
    g=Node(12)
    h=Node(10,right=g)
    f=Node(8,left=e,right=h)
    root=Node(4, left=d,right=f)

    a1=Node(1)
    c1=Node(3)
    d1=Node(2,left=a1, right=c1)
    e1=Node(6)
    g1=Node(12)
    b1=Node(9)
    h1=Node(10,left=b1,right=g1)
    f1=Node(8,left=e1, right=h1)
    root1=Node(4,left=d1,right=f1)

    def testFalse(self):
        output=Validate(self.root)
        self.assertFalse(output)
        self.assertFalse(Validate(None))

    def testTrue(self):
        output=Validate(self.root1)
        self.assertTrue(output)

if __name__ == '__main__':
    unittest.main()

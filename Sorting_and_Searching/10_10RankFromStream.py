class Node:
    def __init__(self, x, left=None, right=None, p=None):
        self.x = x
        self.left = left
        self.right = right
        self.p = p
        self.size = 0

class Tree:
    def __init__(self, root=None):
        self.root = root

    def insert(self, x):
        newNode = Node(x)
        itera = self.root
        y = None
        while itera:
            y = itera
            if newNode.x < itera.x:
                itera = itera.left
            else:
                itera = itera.right

        if not y:
            self.root = newNode
        elif newNode.x < y.x:
            y.left = newNode
        else:
            y.right = newNode
        newNode.p = y

        while newNode:
            newNode.size += 1
            newNode = newNode.p

    def getRank(self, value)->int:
        itera = self.root
        while itera:
            if value == itera.x:
                break
            elif value < itera.x:
                itera = itera.left
            else:
                itera = itera.right
        if not itera:
            return -1

        count = 1
        if itera.left:
            count += itera.left.size
        while itera.p:
            if itera == itera.p.right:
                count += 1
                if itera.p.left:
                    count += itera.p.left.size
            itera = itera.p

        return count


if __name__ == '__main__':
    tree = Tree()
    tree.insert(5)
    tree.insert(1)
    tree.insert(4)
    tree.insert(4)
    tree.insert(5)
    tree.insert(9)
    tree.insert(7)
    tree.insert(13)
    tree.insert(3)

    print(tree.getRank(13))
    print(tree.getRank(4))





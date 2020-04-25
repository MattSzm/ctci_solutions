class Node:
    def __init__(self, key):
        self.k = key
        self.right = None
        self.left = None



def Minimal_Tree(arr):
    return Min_f(arr, 0 ,len(arr)-1)

def Min_f(arr, p, q):
    if q < p:
        return
    else:
        m = int((p+q)/2)
        n = Node(arr[m])
        n.left = Min_f(arr, p, m-1)
        n.right = Min_f(arr, m+1, q)
        return n


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    root = Minimal_Tree(arr)
    print(root.k)
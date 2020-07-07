
class Node:
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev


class Cache:
    def __init__(self, maxSize = 4):
        self.maxSize = maxSize
        self.hashMap = {}
        self.llHead = None
        self.llTail = None
        self.counter = 0

    def insert(self, key, value):
        newNode = Node(key, value)
        if not self.llHead and not self.llTail:
            self.llHead = newNode
            self.llTail = newNode
            self.hashMap[key] = newNode
            self.counter += 1
            return

        if self.counter == self.maxSize:
            lastNode = self.llTail
            lastButOne = lastNode.prev
            self.llTail = lastButOne
            del self.hashMap[lastNode.key]
            self.counter -= 1

        self.llHead.prev = newNode
        newNode.next = self.llHead
        self.llHead = newNode
        self.hashMap[key] = newNode
        self.counter += 1

    def retrieve(self, key):
        returnedNode = self.hashMap[key]
        self.updating_most_recently_used(returnedNode)
        return returnedNode

    def finding_least_recently_used(self):
        returnedNode = self.llTail
        self.updating_most_recently_used(returnedNode)
        return returnedNode

    def updating_most_recently_used(self, node):
        if node.prev and node.next:
            node.prev.next = node.next
            node.next.prev = node.prev
        elif node.prev:
            node.prev.next = None
            self.llTail = node.prev
        elif node.next:
            return
        self.llHead.prev = node
        node.next = self.llHead
        self.llHead = node


if __name__ == '__main__':
    cache = Cache()
    cache.insert('a', 'aaaa')
    cache.insert('b', 'bbbb')
    cache.insert('c', 'cccc')
    print(cache.finding_least_recently_used().value)
    print(cache.llHead.value)
    cache.insert('d','ddd')
    print(cache.llHead.value)
    print(cache.retrieve('c').value)
    print(cache.llHead.value)
    print(cache.llTail.value)
    cache.insert('e','eeee')
    print(cache.llHead.value)
    print(cache.llTail.value)
    print(cache.finding_least_recently_used().value)
    print(cache.llHead.value)
    print(cache.hashMap)

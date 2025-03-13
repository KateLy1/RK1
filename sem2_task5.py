class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None

class Queue:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1
    def pop(self):
        if self.head.next == self.tail:
            return None
        pop_result = self.tail.prev
        self.tail.prev = pop_result.prev
        pop_result.prev.next = pop_result.next
        pop_result.next = None
        pop_result.prev = None
        self.size -= 1
        return pop_result.data
    def peek(self):
        if self.head.next == self.tail:
            return None
        return self.tail.prev.data
    def getSize(self):
        return self.size


def isSubsequence(a, b):
    q = Queue()
    for el in a:
        q.push(el)
    for el in b:
        if q.peek() == el:
            q.pop()
    return q.getSize() == 0


a = "a"
b = "abc"
print(isSubsequence(a, b))

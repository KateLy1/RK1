class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None
    def __str__(self):
        return str(self.data)
    
class deque():
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0
    def push_front(self, value):
        new_node = Node(value)
        new_node.next = self.head.next
        new_node.prev = self.head
        self.head.next.prev = new_node
        self.head.next = new_node
        self.size += 1
    def pop_back(self):
        if self.head.next == self.tail:
            return None
        pop_result = self.tail.prev
        self.tail.prev = pop_result.prev
        pop_result.prev.next = pop_result.next
        pop_result.next = None
        pop_result.prev = None
        self.size -= 1
        return pop_result.data
    def push_back(self, value):
        new_node = Node(value)
        new_node.prev = self.tail.prev
        self.tail.prev.next = new_node
        self.tail.prev = new_node
        new_node.next = self.tail
        self.size += 1
    def pop_front(self):
        if self.tail.prev == self.head:
            return None
        pop_result = self.head.next
        self.head.next = pop_result.next
        pop_result.next.prev = pop_result.prev
        pop_result.next = None
        pop_result.prev = None
        self.size -= 1
        return pop_result.data

  def is_palindrome_deque(text):
    d = deque()
    for char in text:
        d.push_back(char)
    while d.size > 1:
        if d.pop_front() != d.pop_back():
            return False
    return True

print(is_palindrome_deque("madam"))  # True
print(is_palindrome_deque("racecar"))  # True
print(is_palindrome_deque("hello"))  # False
print(is_palindrome_deque("rotor")) # True
print(is_palindrome_deque("ro")) # False

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack(object):
    def __init__(self):
        self.top = None
        
    def push(self, data):
        new_node = Node(data)
        if not self.top:
            self.top = new_node
            return
        
        new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if not self.top:
            return None
        top = self.top
        if self.top.next is not None:
            self.top = self.top.next
        else:
            self.top = None
        return top.data

def isPalindrome(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    for char in s:
        if char != stack.pop():
            return False
    return True

c = "aba"
print(isPalindrome(c))

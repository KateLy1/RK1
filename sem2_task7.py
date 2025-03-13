#Является ли слово палиндромом с помощью стека

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

import unittest
class TestIsPalindrome(unittest.TestCase):

    def test1(self):
        self.assertTrue(isPalindrome(""))

    def test2(self):
        self.assertTrue(isPalindrome("a"))

    def test3(self):
        self.assertTrue(isPalindrome("aba"))

    def test4(self):
        self.assertTrue(isPalindrome("abba"))

    def test5(self):
        self.assertFalse(isPalindrome("abc"))

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

#Необходимо написать функцию, которая принимает на вход односвязный список и разворачивает его.

class Node:
    def __init__(self, data = None, next_Node = None):
        self.data = data
        self.next_Node = next_Node
    def __str__(self):
        return str(self.data)
class Linkedlist:
    head_Node = None
    def __init__(self, head_Node):
        self.head_Node = head_Node
    def __str__(self):
        nodes = []
        current = self.head_Node
        while current:
            nodes.append(str(current.data))
            current = current.next_Node
        return " -> ".join(nodes)

def reversedLinkedList(head):
    prev = None
    current = head
    while (current != None):
        next_Node = current.next_Node
        current.next_Node = prev
        prev = current
        current = next_Node
    head = prev
    return head

import unittest

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next_Node
    return result

class TestReverseLinkedList(unittest.TestCase):

    def test1(self):
        self.assertIsNone(reversedLinkedList(None))

    def test2(self):
        head = Node(1)
        reversed_head = reversedLinkedList(head)
        self.assertEqual(linked_list_to_list(reversed_head), [1])

    def test3(self):
        head = Node(1, Node(2))
        reversed_head = reversedLinkedList(head)
        self.assertEqual(linked_list_to_list(reversed_head), [2, 1])

    def test4(self):
        head = Node(1, Node(2, Node(3)))
        reversed_head = reversedLinkedList(head)
        self.assertEqual(linked_list_to_list(reversed_head), [3, 2, 1])

    def test5(self):
        head = Node(1, Node(2, Node(3, Node(4))))
        reversed_head = reversedLinkedList(head)
        self.assertEqual(linked_list_to_list(reversed_head), [4, 3, 2, 1])
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

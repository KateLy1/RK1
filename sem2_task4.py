#Необходимо написать функцию, которая принимает на вход односвязный список и некоторое целое число val. 
#Необходимо удалить узел из списка, значение которого равно val.


class Node:
    def __init__(self, data = None, next_Node = None):
        self.data = data
        self.next_Node = next_Node
    def __str__(self):
        return str(self.data)
    
def removeElements(head, val):
    dummy = Node()
    dummy.next_Node = head
    prev = dummy
    cur = head

    while (cur != None):
        if (cur.data == val):
            prev.next_Node = cur.next_Node
        else:
            prev = cur
        cur = cur.next_Node
    return dummy.next_Node

import unittest

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next_Node
    return result

class TestRemoveElements(unittest.TestCase):

    def test1(self):
        self.assertIsNone(removeElements(None, 5))

    def test2(self):
        head = Node(5)
        result_head = removeElements(head, 5)
        self.assertIsNone(result_head)

    def test3(self):
        head = Node(3)
        result_head = removeElements(head, 5)
        self.assertEqual(linked_list_to_list(result_head), [3])

    def test4(self):
        head = Node(5, Node(3, Node(7)))
        result_head = removeElements(head, 5)
        self.assertEqual(linked_list_to_list(result_head), [3, 7])

    def test5(self):
        head = Node(1, Node(2, Node(3, Node(2, Node(5)))))
        result_head = removeElements(head, 2)
        self.assertEqual(linked_list_to_list(result_head), [1, 3, 5])

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

#Дан связный список. Необходимо найти середину списка. Сделать это необходимо за O(n) без дополнительных аллокаций

def middleNode(head):
    slow = fast = head
    while fast != None and fast.next_Node != None:
        slow = slow.next_Node
        fast = fast.next_Node.next_Node
    return slow

import unittest

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next_Node
    return result

class TestMiddleNode(unittest.TestCase):

    def test1(self):
        self.assertIsNone(middleNode(None))

    def test2(self):
        head = Node(1)
        middle = middleNode(head)
        self.assertEqual(middle.data, 1)

    def test3(self):
        head = Node(1, Node(2))
        middle = middleNode(head)
        self.assertEqual(middle.data, 2)

    def test4(self):
        head = Node(1, Node(2, Node(3)))
        middle = middleNode(head)
        self.assertEqual(middle.data, 2)

    def test5(self):
        head = Node(1, Node(2, Node(3, Node(4))))
        middle = middleNode(head)
        self.assertEqual(middle.data, 3)
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

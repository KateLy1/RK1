#Дан односвязный список. Необходимо проверить, является ли этот список циклическим.

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

def hasCycle(head):
    if (head  == None) or (head.next_Node == None):
        return False
    slow = head
    fast = head.next_Node
    while slow != fast:
        if fast == None or fast.next_Node == None:
            return False
        slow = slow.next_Node
        fast = fast.next_Node.next_Node
    return True


import unittest
class TestHasCycle(unittest.TestCase):

    def test1(self):
        self.assertFalse(hasCycle(None))

    def test2(self):
        node = Node(1)
        self.assertFalse(hasCycle(node))

    def test3(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node1.next_Node = node2
        node2.next_Node = node3
        self.assertFalse(hasCycle(node1))

    def test4(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node1.next_Node = node2
        node2.next_Node = node3
        node3.next_Node = node1
        self.assertTrue(hasCycle(node1))

    def test5(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node1.next_Node = node2
        node2.next_Node = node3
        node3.next_Node = node2
        self.assertTrue(hasCycle(node1))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

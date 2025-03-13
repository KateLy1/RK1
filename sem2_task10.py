#Написать функцию, которая принимает на вход два отсортированных односвязных списка и объединяет их в один отсортированный список. 
#При этом затраты по памяти должны быть O(1)


class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next = next_node
    def __str__(self):
        return str(self.data)    
    
    def __str__(self):
        nodes = []
        current = self.head_Node
        while current:
            nodes.append(str(current.data))
            current = current.next_Node
        return " -> ".join(nodes)

def merge_sorted_lists(head1, head2):
    if head1 == None:
        return head2
    if head2 == None:
        return head1
    if head1.data <= head2.data:
        head = head1
        head1 = head1.next
    else:
        head = head2
        head2 = head2.next
    current = head
    while head1 != None and head2 != None:
        if head1.data <= head2.data:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next
    if head1:
        current.next = head1
    elif head2:
        current.next = head2
    return head

import unittest
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.data)
        current = current.next
    return result

class TestMergeSortedLists(unittest.TestCase):

    def test1(self):
        self.assertIsNone(merge_sorted_lists(None, None))

    def test2(self):
        node1 = Node(1)
        node2 = Node(2)
        node1.next = node2
        
        result_head = merge_sorted_lists(node1, None)
        self.assertEqual(linked_list_to_list(result_head), [1, 2])

        result_head = merge_sorted_lists(None, node1)
        self.assertEqual(linked_list_to_list(result_head), [1, 2])


    def test3(self):
        node1 = Node(1)
        node2 = Node(3)
        node1.next = node2

        node3 = Node(2)
        node4 = Node(4)
        node3.next = node4

        result_head = merge_sorted_lists(node1, node3)
        self.assertEqual(linked_list_to_list(result_head), [1, 2, 3, 4])

    def test4(self):
        node1 = Node(1)
        node2 = Node(4)
        node1.next = node2

        node3 = Node(2)
        node4 = Node(3)
        node3.next = node4

        result_head = merge_sorted_lists(node1, node3)
        self.assertEqual(linked_list_to_list(result_head), [1, 2, 3, 4])
        
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)



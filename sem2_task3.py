def middleNode(head):
    slow = fast = head
    while fast != None and fast.next_Node != None:
        slow = slow.next_Node
        fast = fast.next_Node.next_Node
    return slow

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(1)
node5 = Node(3)
node1.next_Node = node2
node2.next_Node = node3
node3.next_Node = node4
node4.next_Node = node5
list_a = Linkedlist(node1)
print(middleNode(list_a.head_Node))

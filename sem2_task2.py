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

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(1)
node5 = Node(3)
node6 = Node(20)
node1.next_Node = node2
node2.next_Node = node3
node3.next_Node = node4
node4.next_Node = node5
node5.next_Node = node6
list_a = Linkedlist(node1)
print(list_a)
list_a.head_Node = reversedLinkedList(list_a.head_Node)
print(list_a)

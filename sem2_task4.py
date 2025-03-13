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

removeElements(list_a.head_Node, 1)
print(list_a)

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
node6.next_Node = node2
list_a = Linkedlist(node1)
print(hasCycle(list_a.head_Node))

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

# Создаем несколько отсортированных списков для тестов
def create_linked_list(data_list):
    if not data_list:
        return None
    head = Node(data_list[0])
    current = head
    for data in data_list[1:]:
        current.next = Node(data)
        current = current.next
    return head

# Пример 1
list1 = create_linked_list([1, 3, 5, 7])
list2 = create_linked_list([2, 4, 6, 8])
merged_list = merge_sorted_lists(list1, list2)

# Выводим объединенный список (для проверки)
current = merged_list
result_list = []
while current:
    result_list.append(current.data)
    current = current.next
print(result_list)  # Ожидаемый вывод: [1, 2, 3, 4, 5, 6, 7, 8]


# Пример 2: один список пустой
list3 = create_linked_list([10, 20, 30])
list4 = None
merged_list2 = merge_sorted_lists(list3, list4)

current = merged_list2
result_list = []
while current:
    result_list.append(current.data)
    current = current.next
print(result_list)  # Ожидаемый вывод: [10, 20, 30]

# Пример 3:  Оба списка пустые
list5 = None
list6 = None
merged_list3 = merge_sorted_lists(list5, list6)

current = merged_list3
if current is None:
    print("None") # Ожидаемый вывод: None
else:
  result_list = []
  while current:
      result_list.append(current.data)
      current = current.next
  print(result_list)


# Пример 4: один список содержит только одно значение
list7 = create_linked_list([5])
list8 = create_linked_list([1, 2, 3, 4, 6, 7])
merged_list4 = merge_sorted_lists(list7, list8)

current = merged_list4
result_list = []
while current:
    result_list.append(current.data)
    current = current.next
print(result_list) # Ожидаемый вывод: [1, 2, 3, 4, 5, 6, 7]


# Пример 5: оба списка содержат одно и то же значение, по одному разу
list9 = create_linked_list([5])
list10 = create_linked_list([5])
merged_list5 = merge_sorted_lists(list9, list10)

current = merged_list5
result_list = []
while current:
    result_list.append(current.data)
    current = current.next
print(result_list)  # Ожидаемый вывод: [5, 5]

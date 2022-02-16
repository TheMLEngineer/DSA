class Node:
    def __init__(self , value) -> None:
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self , value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp)
            temp = temp.next

my_linked_list = LinkedList(4)

print(my_linked_list.head.value)



print(my_linked_list.print_list())

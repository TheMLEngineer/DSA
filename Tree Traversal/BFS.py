class Node:
    def __init__(self , value) -> None:
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self , value):
        new_node = Node(value)
        # If BST is empty
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        # If BST is not empty
        while True:
            # returning true and false in while loop to exit while loop
            #Using temp pointer
            # If new value already exist in tree we don't add
            if new_node.value == temp.value:
                return False
            # Ading element in left side
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                # If the point to add value is not in current left level , we are pointing to next left level
                temp = temp.left
            # Adding element in right side
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                # If the point to add value is not in current right level , we are pointing to next right level
                temp = temp.right

    def contains(self , value):
        if self.root is None:
            return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        # When item not found in while loop , the while loop breaks and it returns false
        return False

    def min_value_node(self , current_node):
        while current_node.left is not None:
            current_node = current_node.left
        # If we need node value
        # return current_node.value
        # returning node
        return current_node

    




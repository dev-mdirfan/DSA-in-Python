# Insert node at middle

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.last_node = None
    
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must in Linked List!")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

# 
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def insertAfter(self, given_node, new_data):
        new_node = Node(new_data)
        temp = given_node.next
        given_node.next = new_node
        new_node.next = temp

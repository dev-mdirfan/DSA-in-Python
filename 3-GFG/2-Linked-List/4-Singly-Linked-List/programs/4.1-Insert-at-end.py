#  Insert a node in the end of the linked list

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def insertEnd(self, data):
        new_node = Node(data)
        temp = self.head
        
        while temp.next != None:
            temp = temp.next
        
        temp.next = new_node

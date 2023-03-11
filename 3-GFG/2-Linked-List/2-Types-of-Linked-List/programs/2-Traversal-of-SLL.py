# Traversal of SLL

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None
        self.last_node = None
    
    def append(self, data):
        # if linked list is empty then last_node will be none so in if condition head will be created
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            # adding node to the tail of linked list
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
    
    def display(self):
        current = self.head
        
        while current is not None:
            print(current.data, end=', ')
            current = current.next
        print()

if __name__ == '__main__':
    L = LinkedList()
    
    L.append(1)
    L.append(2)
    L.append(3)
    L.append(4)
    L.append(5)
    L.display()

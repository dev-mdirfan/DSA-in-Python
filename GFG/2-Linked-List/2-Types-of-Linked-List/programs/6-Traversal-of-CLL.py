# Traversal CLL

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.last_node = None
    
    def append(self, data):
        # is circular linked list is empty then last_node will be none so in if condition head will be created
        if self.last_node is None:
            self.head = Node(data)
            self.last_node =self.head
        # adding node to the tail of circular linked list
        else:
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next
            self.last_node.next = self.head
    
    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end=' ')
            current = current.next
            if current == self.head:
                break
        print()

if __name__ == '__main__':
    L = CircularLinkedList()
    L.append(12)
    L.append(54)
    L.append(3)
    L.append(77)
    
    L.display()
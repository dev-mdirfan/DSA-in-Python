#  Traversal of HLL

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class HeaderLinkedList:
    def __init__(self) -> None:
        self.head = Node(0)
        self.last_node = self.head
    
    def append(self, data):
        self.last_node.next = Node(data)
        self.last_node = self.last_node.next
    
    def display(self):
        current = self.head.next
        
        while current is not None:
            print(current.data, end=' ')
            current = current.next
        print()

if __name__ == '__main__':
    L = HeaderLinkedList()
    L.append(11)
    L.append(12)
    L.append(13)
    L.display()
    
    L.append(14)
    L.append(15)
    L.display()

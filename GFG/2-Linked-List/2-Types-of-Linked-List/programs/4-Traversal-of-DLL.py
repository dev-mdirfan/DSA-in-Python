# Traversal of DLL

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.start_node = None
        self.last_node = None
    
    def append(self, data):
        if self.last_node is None:
            self.head = Node(data)
            self.last_node = self.head
        else:
            new_node = Node(data)
            self.last_node.next = new_node
            new_node.previous = self.last_node
            new_node.next = None
            self.last_node = new_node
    
    def display(self,Type):
        if Type == 'Left_To_Right':
            current = self.head
            print(Type,':')
            while current is not None:
                print(current.data, end=' ')
                current = current.next
            print()
        else:
            current = self.last_node
            print(Type,':')
            while current is not None:
                print(current.data, end = ' ')
                current = current.previous
            print()

if __name__ == "__main__":
    L = DoublyLinkedList()
    L.append(10)
    L.append(20)
    L.append(30)
    L.append(40)
    L.append(50)
    
    L.display('Left_To_Right')
    L.display('Right_To_Left')

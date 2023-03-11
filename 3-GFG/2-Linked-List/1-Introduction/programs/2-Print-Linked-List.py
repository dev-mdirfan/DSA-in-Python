# Printing elements of the linked list (Traversal of LL)

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def PrintList(self):
        temp = self.head
        
        while temp != None:
            print(temp.data, end=' ')
            temp = temp.next

if __name__ == '__main__':
    
    List1 = LinkedList()
    
    List1.head = Node(1)
    second = Node(2)
    third = Node(3)
    
    List1.head.next = second
    second.next = third
    
    List1.PrintList()


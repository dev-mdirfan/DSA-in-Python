# Linked List Representation in Python

class node:
    def __init__(self, data):
        self.data = data # Assigning data
        self.next = None # Initializing next as Null

class LinkedList:
    def __init__(self) -> None:
        self.head = None

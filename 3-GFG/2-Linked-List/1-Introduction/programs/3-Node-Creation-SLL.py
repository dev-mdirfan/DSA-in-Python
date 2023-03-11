# Creating Node

class Node:
    def __init__(self, data = 0) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

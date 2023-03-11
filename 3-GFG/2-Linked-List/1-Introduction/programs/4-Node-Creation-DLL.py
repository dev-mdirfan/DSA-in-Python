# Doubly Linked List Node Creation

class Node:
    def __init__(self, next=None, prev=None, data=None) -> None:
        self.data = data
        self.prev = prev
        self.next = next

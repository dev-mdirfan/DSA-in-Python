# Singly Linked List

- [Singly Linked List](#singly-linked-list)
- [1. Insertion in Linked List](#1-insertion-in-linked-list)
  - [Add a node at the front: (4 steps process)](#add-a-node-at-the-front-4-steps-process)
  - [Add a node after a given node: (5 steps process)](#add-a-node-after-a-given-node-5-steps-process)
  - [Add a node at the end: (6 steps process)](#add-a-node-at-the-end-6-steps-process)


# 1. Insertion in Linked List

|Question Name|Platform 1|
|---|---|
|Linked List Insertion|[GFG](https://practice.geeksforgeeks.org/problems/linked-list-insertion-1587115620/1?utm_source=gfg&utm_medium=article&utm_campaign=bottom_sticky_on_article)|

We have introduced Linked Lists in the previous post. We also created a simple linked list with 3 nodes and discussed linked list traversal.

All programs discussed in this post consider the following representations of the linked list. 

```py
# Node Class

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
```

In this post, methods to insert a new node in the linked list are discussed. A node can be added in three ways 

- At the front of the linked list  
- After a given node. 
- At the end of the linked list.

## Add a node at the front: (4 steps process) 

__Approach:__ 

The new node is always added before the head of the given Linked List. And newly added node becomes the new head of the Linked List. For example, if the given Linked List is 10->15->20->25 and we add an item 5 at the front, then the Linked List becomes 5->10->15->20->25. Let us call the function that adds at the front of the list is push(). The push() must receive a pointer to the head pointer because the push must change the head pointer to point to the new node

![Linked List Insert at start](../images/Linkedlist_insert_at_start.png)

Following are the 4 steps to add a node at the front.

```py
# Insert new node at start

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.last_node = None
        
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
```

__Complexity Analysis:__

- __Time Complexity:__ O(1), We have a pointer to the head and we can directly attach a node and change the pointer. So the Time complexity of inserting a node at the head position is O(1) as it does a constant amount of work.
- __Auxiliary Space:__ O(1)

## Add a node after a given node: (5 steps process) 

__Approach:__ We are given a pointer to a node, and the new node is inserted after the given node.

Follow the steps to add a node after a given node:

- Firstly, check if the given previous node is NULL or not.
- Then, allocate a new node and
- Assign the data to the new node
- And then make the next of new node as the next of previous node. 
- Finally, move the next of the previous node as a new node.

![Linked List insert at middle](../images/Linkedlist_insert_middle.png)

```py
# Insert node at middle

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.last_node = None
    
    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("The given previous node must in Linked List!")
            return
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
```

__Complexity Analysis:__

__Time complexity:__ O(1), since prev_node is already given as argument in a method, no need to iterate over list to find prev_node

__Auxiliary Space:__ O(1) since using constant space to modify pointers

## Add a node at the end: (6 steps process) 

- The new node is always added after the last node of the given Linked List. For example if the given Linked List is 5->10->15->20->25 and we add an item 30 at the end, then the Linked List becomes 5->10->15->20->25->30. 
- Since a Linked List is typically represented by the head of it, we have to traverse the list till the end and then change the next to last node to a new node.

![Inset Last](../images/Linkedlist_insert_last.png)

Following are the 6 steps to add a node at the end.




# Introduction

## What is Linked List

Like arrays, a Linked List is a linear data structure. Unlike arrays, linked list elements are not stored at a contiguous location; the elements are linked using pointers.
They include a series of connected nodes. Here, each node stores the data and the address of the next node.

![Linked List](../images/Linkedlist.png)

### Why Linked List?

Arrays can be used to store linear data of similar types, but arrays have the following limitations:

1. __The size of the arrays is fixed:__ So we must know the upper limit on the number of elements in advance. Also, generally, the allocated memory is equal to the upper limit irrespective of the usage.
2. __Insertion of a new element / Deletion of a existing element in an array of elements is expensive:__ The room has to be created for the new elements and to create room existing elements have to be shifted but in Linked list if we have the head node then we can traverse to any node through it and insert new node at the required position.

__Example:__
In a system, if we maintain a sorted list of IDs in an array id[] = [1000, 1010, 1050, 2000, 2040].
If we want to insert a new ID 1005, then to maintain the sorted order, we have to move all the elements after 1000 (excluding 1000).
Deletion is also expensive with arrays until unless some special techniques are used. For example, to delete 1010 in id[], everything after 1010 has to be moved due to this so much work is being done which affects the efficiency of the code.

### Advantages of Linked Lists over arrays:

1. Dynamic Array.
2. Ease of Insertion/Deletion.

### Drawbacks of Linked Lists:

1. Random access is not allowed. We have to access elements sequentially starting from the first node(head node). So we cannot do a binary search with linked lists efficiently with its default implementation.
2. Extra memory space for a pointer is required with each element of the list.
3. Not cache-friendly. Since array elements are contiguous locations, there is the locality of reference which is not there in the case of linked lists.
4. It takes a lot of time in traversing and changing the pointers.
5. Reverse traversing is not possible in singly linked lists.
6. It will be confusing when we work with pointers.
7. Direct access to an element is not possible in a linked list as in an array by index.
8. Searching for an element is costly and requires O(n) time complexity.
9. Sorting of linked lists is very complex and costly.

### Types of Linked Lists:

1. __Simple Linked List__ – In this type of linked list, one can move or traverse the linked list in only one direction. where the next pointer of each node points to other nodes but the next pointer of the last node points to NULL. It is also called “Singly Linked List”.
2. __Doubly Linked List__ – In this type of linked list, one can move or traverse the linked list in both directions (Forward and Backward)
3. __Circular Linked List__ – In this type of linked list, the last node of the linked list contains the link of the first/head node of the linked list in its next pointer.
4. __Doubly Circular Linked List__ – A Doubly Circular linked list or a circular two-way linked list is a more complex type of linked list that contains a pointer to the next as well as the previous node in the sequence. The difference between the doubly linked and circular doubly list is the same as that between a singly linked list and a circular linked list. The circular doubly linked list does not contain null in the previous field of the first node.
5. __Header Linked List__ – A header linked list is a special type of linked list that contains a header node at the beginning of the list. 

### Basic operations on Linked Lists:

1. Deletion
2. Insertion
3. Search
4. Display

### Representation of Singly Linked Lists:

A linked list is represented by a pointer to the first node of the linked list. The first node is called the head of the linked list. If the linked list is empty, then the value of the head points to NULL.

Each node in a list consists of at least two parts:

1. A Data Item (we can store integers, strings, or any type of data).
2. Pointer (Or Reference) to the next node (connects one node to another) or An address of another node.

- In C, we can represent a node using structures. Below is an example of a linked list node with integer data.
- In Java or C#, LinkedList can be represented as a class and a Node as a separate class. The LinkedList class contains a reference of Node class type. 

### Implementation

```py

```

### Construction of a simple linked list with 3 nodes:

#### Traversal of a Linked List

In the previous program, we created a simple linked list with three nodes. Let us traverse the created list and print the data of each node. For traversal, let us write a general-purpose function printList() that prints any given list.

#### Practice

|Question Name|Platform 1|Platform 2|
|---|---|---|
|Print Linked List Elements|[GFG](https://practice.geeksforgeeks.org/problems/print-linked-list-elements/1)||

```py

```

```yml
Output: 1  2  3 
```

__Time Complexity:__

|Time Complexity|Worst Case|Average Case|
|---|---|---|
|Search|O(n)|O(n)|
|Insertion|O(1)|O(1)|
|Deletion|O(1)|O(1)|

- Search is O(n) because as data is not stored in contiguous memory locations so we have to traverse one by one.
- Insertion and Deletion are O(1) because we have to just link new nodes for Insertion with the previous and next node and dislink exist nodes for deletion from the previous and next nodes without any traversal.

__Auxiliary Space:__ O(N) [To store dynamic memory]

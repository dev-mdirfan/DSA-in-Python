# 3. linked List

## 3.1 What is a Linked List?

- A linked list is a data structure used for storing collections of data. A linked list has the following properties.
  - Successive elements are connected by pointers.
  - The last element points to NULL.
  - Can grow or shrink in size during execution of a program.
  - Can be made just as long as required (until systems memory exhausts).
  - Does not waste memory space (but takes some extra memory for pointers).

```mermaid
flowchart LR

HEAD --> 4 --> 15 --> 7 --> 40 --> NULL
```

## 3.2 Linked List ADT

The following operations make linked lists an ADT:

__Main Linked Lists Operations :__
- __Insert:__ inserts an element into the list.
- __Delete:__ removes and returns the specified position element from the list.

__Auxiliary Linked Lists Operations :__
- __Delete List:__ removes all elements of the list (dispose of the list)
- __Count:__ returns the number of elements in the list.
- __Find:__ nth node from the end of the list.

## 3.3 Why Linked List ?

There are many other data structures that do the same thing as linked lists. Before discussing linked lists it is important to understand the difference between linked lists and arrays. Both linked lists and arrays are used to store collections of data, and since both are used for the same purpose, we need to differentiate their usage. That means in which cases arrays are suitable and in which cases linked lists are suitable.

## 3.4 Arrays Overview

One memory block is allocated for the entire array to hold the elements of the array. The array elements can be accessed in constant time by using the index of the particular element as the subscript.

|3|2|1|2|2|3|
|---|---|---|---|---|---|
|0|1|2|3|4|5|


__Why Constant Time for Accessing Array Elements ?__

- To access an array element, the address of an element is computed as an offset from the base address of the array and one multiplication is needed to compute what is supposed to be added to the base address to get the memory address of the element.
- First the size of the an element of that data type is calculated and then it is multiplied with the index of the element to get the value to be added to the base address.

__Advantages of Arrays :__

- Simple and easy to use.
- Faster access to the elements (constant access).

__Disadvantages of Arrays :__

- __Fixed size:__ The size of the array is static (specify the array size before using it).
- __One


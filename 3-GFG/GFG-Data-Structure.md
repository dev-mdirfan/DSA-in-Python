### 1. Arrays

#### What is an Array?

- An array is a collection of items of same data type stored at contiguous memory locations. 
- This makes it easier to calculate the position of each element by simply adding an offset to a base value, i.e., the memory location of the first element of the array (generally denoted by the name of the array). The base value is index 0 and the difference between the two indexes is the offset.

- An array is a linear data structure and it is a collection of items stored at contiguous memory locations. The idea is to store multiple items of the same type together in one place. It allows the processing of a large amount of data in a relatively short period. The first element of the array is indexed by a subscript of 0. There are different operations possible in an array, like Searching, Sorting, Inserting, Traversing, Reversing, and Deleting.
- For simplicity, we can think of an array as a fleet of stairs where on each step is placed a value (let’s say one of your friends). Here, you can identify the location of any of your friends by simply knowing the count of the step they are on. 
Remember: “Location of next index depends on the data type we use”. 

![array](images/array-2.png)

#### Is the array always of a fixed size?

- In C language, the array has a fixed size meaning once the size is given to it, it cannot be changed i.e. you can’t shrink it nor can you expand it. The reason was that for expanding if we change the size we can’t be sure ( it’s not possible every time) that we get the next memory location to us for free. The shrinking will not work because the array, when declared, gets memory statically allocated, and thus compiler is the only one that can destroy it.

#### Types of indexing in an array:

- 0 (zero-based indexing): The first element of the array is indexed by a subscript of 0.
- 1 (one-based indexing): The first element of the array is indexed by the subscript of 1.
- n (N-based indexing): The base index of an array can be freely chosen. Usually, programming languages allowing n-based indexing also allow negative index values, and other scalar data types like enumerations, or characters may be used as an array index.

![indexing](images/Array-In-C.png)

#### How an Array is initialized?

By default the array is uninitialized, and no elements of the array are set to any value. However, for the proper working of the array, array initialization becomes important. Array initialization can be done by the following methods:

1. __Passing no value within the initializer:__ One can initialize the array by defining the size of the array and passing no values within the initializer.
   - Syntax: `int arr[ 5 ] = {  };`
2. __By passing specific values within the initializer:__ One can initialize the array by defining the size of the array and passing specific values within the initializer.
   - Syntax: `int arr[ 5 ] = { 1, 2, 3, 4, 5 };`
   - Note: __The count of elements within the “{ }”, must be less than the size of the array__ If the count of elements within the “{ }” is less than the size of the array, the remaining positions are considered to be ‘0’.
   - Syntax: `int arr[ 5 ] = { 1, 2, 3 } ;`
3. __By passing specific values within the initializer but not declaring the size:__ One can initialize the array by passing specific values within the initializer and not particularly mentioning the size, the size is interpreted by the compiler.
   - Syntax: `int arr[  ] = { 1, 2, 3, 4, 5 };`
4. __Universal Initialization:__ After the adoption of universal initialization in C++, one can avoid using the equals sign between the declaration and the initializer.
    ```c
    int arr[ ]  { 1, 2, 3, 4, 5 };
    ```

#### What are the different operations on the array?

Arrays allow random access to elements. This makes accessing elements by position faster. Hence operation like searching, insertion, and access becomes really efficient. Array elements can be accessed using the loops.

##### 1. Insertion in Array:

We try to insert a value to a particular array index position, as the array provides random access it can be done easily using the assignment operator.

###### Pseudo Code:

```c
// to insert a value= 10 at index position 2;

arr[ 2 ] = 10;
```

##### Time Complexity: 

- O(1) to insert a single element
- O(N) to insert all the array elements [where N is the size of the array]

#### 2. Access elements in Array:

Accessing array elements become extremely important, in order to perform operations on arrays.

##### Pseudo Code:

```c
// to access array element at index position 2, we simply can write

return arr[ 2 ] ;
```

##### Time Complexity: O(1)

Here is the code for working in an array:

```py
arr = [1, 2, 3, 4]
 
# accessing element at index 2
print(arr[2])
 
# This code is contributed by ishankhandelwals.
```
__Output:__ 3

#### 3. Searching in Array: 

We try to find a particular value in the array, in order to do that we need to access all the array elements and look for the particular value.

##### Pseudo Code:

```c
// searching for value 2 in the array;

Loop from i = 0 to 5:
    check if  arr[i] = 2:
        return true;
```

##### Time Complexity: O(N), where N is the size of the array.

Here is the code for working with an array:

```py
# code
import array
 
gfg = array.array('i', [1, 2, 3, 4])
 
for gfg2 in gfg:
    print(gfg2)
```
__Output:__ 
1
2 
3 
4

Here the value 5 is printed because the first element has index zero and at the zeroth index, we already assigned the value 5.

#### Types of arrays : 

1. One-dimensional array (1-D arrays)
2. Two Dimension (2D) Array
3. Multidimensional array

#### Advantages of using arrays: 

- Arrays allow random access to elements. This makes accessing elements by position faster.
- Arrays have better cache locality which makes a pretty big difference in performance.
- Arrays represent multiple data items of the same type using a single name.

#### Disadvantages of using arrays: 

- You can’t change the size i.e. once you have declared the array you can’t change its size because of static memory allocation. Here Insertion(s) and deletion(s) are difficult as the elements are stored in consecutive memory locations and the shifting operation is costly too.
- Now if take an example of the implementation of data structure Stack using array there are some obvious flaws. 
- Let’s take the POP operation of the stack. The algorithm would go something like this. 
  - Check for the stack underflow
  - Decrement the top by 1

What we are doing here is, that the pointer to the topmost element is decremented, which means we are just bounding our view, and actually that element stays there taking up the memory space. If you have an array (as a Stack) of any primitive data type then it might be ok. But in the case of an array of Objects, it would take a lot of memory.

__Examples:__

```c
// A character array in C/C++/Java
char arr1[] = {‘g’, ‘e’, ‘e’, ‘k’, ‘s’};

// An Integer array in C/C++/Java
int arr2[] = {10, 20, 30, 40, 50};

// Item at i’th index in array is typically accessed as “arr[i]”.  
For example:
arr1[0] gives us ‘g’
arr2[3] gives us 40
```

Usually, an array of characters is called a ‘string’, whereas an array of ints or floats is simply called an array.

#### Characteristics of an Array:

An array has various characteristics which are as follows:

- Arrays use an index-based data structure which helps to identify each of the elements in an array easily using the index.
- If a user wants to store multiple values of the same data type, then the array can be utilized efficiently.
- An array can also handle complex data structures by storing data in a two-dimensional array.
- An array is also used to implement other data structures like Stacks, Queues, Heaps, Hash tables, etc.
- The search process in an array can be done very easily.

#### Applications of Array: 

- An array is used in solving matrix problems.
- Database records are also implemented by an array.
- It helps in implementing a sorting algorithm.
- It is also used to implement other data structures like Stacks, Queues, Heaps, Hash tables, etc.
- An array can be used for CPU scheduling.
- Can be applied as a lookup table in computers.
- Arrays can be used in speech processing where every speech signal is an array.
- The screen of the computer is also displayed by an array. Here we use a multidimensional array. 
- The array is used in many management systems like a library, students, parliament, etc. 
- The array is used in the online ticket booking system. Contacts on a cell phone are displayed by this array.
- In games like online chess, where the player can store his past moves as well as current moves. It indicates a hint of position. 
- To save images in a specific dimension in the android Like 360*1200
- Array stores data elements of the same data type.
- Arrays are used when the size of the data set is known.
- Used in solving matrix problems.
- Applied as a lookup table in computer.
- Databases records are also implemented by the array.
- Helps in implementing sorting algorithm.
- The different variables of the same type can be saved under one name.
- Arrays can be used for CPU scheduling.
- Used to Implement other data structures like Stacks, Queues, Heaps, Hash tables, etc.

#### Real-Life Applications of Array: 

- An array is frequently used to store data for mathematical computations.
- It is used in image processing.
- It is also used in record management.
- Book pages are also real-life examples of an array.
- It is used in ordering boxes as well.

#### Frequently asked questions (FAQs) about Array Data Structures

1. What is an array in data structure with example?
   - An array is a collection of items of the same data type stored at contiguous memory locations. Ex. int arr[5] = {1, 2, 3, 4, 5};
2. What are the 3 types of arrays?
   1. Indexed arrays
   2. Multidimensional arrays
   3. Associative arrays
3. What data structure is an array?
   - An array is a linear data structure.
4. Difference between array and structure?
   - The structure can contain variables of different types but an array only contain variables of the same type.

### 2. Linked list: 

A linked list is a linear data structure in which elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers as shown in the below image: 

Types of linked lists:

- Singly-linked list
- Doubly linked list
- Circular linked list
- Doubly circular linked list

![ll](images/Linkedlist1.png)

#### Characteristics of a Linked list: 

- A linked list uses extra memory to store links.
- During the initialization of the linked list, there is no need to know the size of the elements.
- Linked lists are used to implement stacks, queues, graphs, etc.
- The first node of the linked list is called the Head.
- The next pointer of the last node always points to NULL.
- In a linked list, insertion and deletion are possible easily.
- Each node of the linked list consists of a pointer/link which is the address of the next node.
- Linked lists can shrink or grow at any point in time easily.


#### Applications of the Linked list:

- Linked lists are used to implement stacks, queues, graphs, etc.
- Linked lists are used to perform arithmetic operations on long integers.
- It is used for the representation of sparse matrices.
- It is used in the linked allocation of files.
- It helps in memory management.
- It is used in the representation of Polynomial Manipulation where each polynomial term represents a node in the linked list.
- Linked lists are used to display image containers. Users can visit past, current, and next images.
- They are used to store the history of the visited page.
- They are used to perform undo operations.
- Linked are used in software development where they indicate the correct syntax of a tag.
- Linked lists are used to display social media feeds.

#### Real-Life Applications of a Linked list: 

- A linked list is used in Round-Robin scheduling to keep track of the turn in multiplayer games.
- It is used in image viewer. The previous and next images are linked, and hence can be accessed by the previous and next buttons.
- In a music playlist, songs are linked to the previous and next songs. 




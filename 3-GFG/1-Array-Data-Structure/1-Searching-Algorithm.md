# Searching Algorithms

## 0. What is searching algorithm?

Searching Algorithms are designed to check for an element or retrieve an element from any data structure where it is stored.

Based on the type of search operation, these algorithms are generally classified into two categories:

1. __Sequential Search:__ In this, the list or array is traversed sequentially and every element is checked. For example: Linear Search.
- Linear Search to find the element “20” in a given list of numbers.
- ![LinearSearch](images/Linear-Search1.png)
2. __Interval Search:__ These algorithms are specifically designed for searching in sorted data-structures. These type of searching algorithms are much more efficient than Linear Search as they repeatedly target the center of the search structure and divide the search space in half. For Example: Binary Search.
- Binary Search to find the element “23” in a given list of numbers
- ![BinarySearch](images/BinarySearch.png)

## 1. Linear Search

- Linear search is the simplest method for searching.
- In Linear search technique of searching; the element to be found in searching the elements to be found is searched sequentially in the list.
- This method can be performed on a sorted or an unsorted list (usually arrays). In case of a sorted list searching starts from 0th element and continues until the element is found from the list or the element whose value is greater than (assuming the list is sorted in ascending order), the value being searched is reached.
- As against this, searching in case of unsorted list also begins from the 0th element and continues until the element or the end of the list is reached. The linear search algorithm searches all elements in the array sequentially. Its best execution time is 1, whereas the worst execution time is n, where n is the total number of items in the search array.
-  It is the most simple search algorithm in data structure and checks each item in the set of elements until it matches the search element until the end of data collection. When data is unsorted, a linear search algorithm is preferred.
-  Linear Search is defined as a sequential search algorithm that starts at one end and goes through each element of a list until the desired element is found, otherwise the search continues till the end of the data set. It is the easiest searching algorithm

![Linear Search](images/Linear-Search1.png)

### linear Search Algorithm

__Step 1:__ First, read the search element (Target element) in the array.
__Step 2:__ In the second step compare the search element with the first element in the array.
__Step 3:__ If both are matched, display “Target element is found” and terminate the Linear Search 
function.
__Step 4:__ If both are not matched, compare the search element with the next element in the array.
__Step 5:__ In this step, repeat steps 3 and 4 until the search (Target) element is compared with the 
last element of the array.
__Step 6:__ If the last element in the list does not match, the Linear Search Function will be 
terminated, and the message “Element is not found” will be displayed.

### Question: Given an array arr[] of N elements, the task is to write a function to search a given element x in arr[].

__Input:__ arr[] = {10, 20, 80, 30, 60, 50,110, 100, 130, 170}, x = 110;
__Output:__ 6
__Explanation:__ Element x is present at index 6

__Input:__ arr[] = {10, 20, 80, 30, 60, 50,110, 100, 130, 170}, x = 175;
__Output:__ -1
__Explanation:__ Element x is not present in arr[].

__Follow the below idea to solve the problem:__

Iterate from 0 to N-1 and compare the value of every index with x if they match return index

 Follow the given steps to solve the problem:

1. Set the first element of the array as the current element.
2. If the current element is the target element, return its index.
3. If the current element is not the target element and if there are more elements in the array, set the current element to the next element and repeat step 2.
4. If the current element is not the target element and there are no more elements in the array, return -1 to indicate that the element was not found.

Below is the implementation of the above approach:



# Dutch National Flag Problem
# https://www.geeksforgeeks.org/sort-an-array-of-0s-1s-and-2s/
# We are given an array which contains only 0s, 1s and 2s. Write a program to sort the array without using any sorting algorithm.
# This problem proposed by Edsger W. Dijkstra, the Dutch computer scientist. Hence the name!
# This problem is also called 3-way partitioning problem.
# Another variation of this problem is given n buckets, each containing some red, white or blue balls, arrange the balls such that the balls of same color are placed together and their collective color group is in order red, white and blue.
# [0, 0, 0, 1, 1, 1, 1, 2, 0, 1, 1, 0, 2, 1, 2, 0]


# Time Complexity: O(nlogn) using sorting algorithm
# Space Complexity: O(1)
def sort_array(arr):
    arr.sort()
    return arr


# Time Complexity: O(n) using counting sort
# Space Complexity: O(1)
def sort_array(arr):
    count_0 = 0
    count_1 = 0
    count_2 = 0
    for i in arr:
        if i == 0:
            count_0 += 1
        elif i == 1:
            count_1 += 1
        else:
            count_2 += 1
    for i in range(count_0):
        arr[i] = 0
    for i in range(count_0, count_0 + count_1):
        arr[i] = 1
    for i in range(count_0 + count_1, count_0 + count_1 + count_2):
        arr[i] = 2
    return arr


# Time Complexity: O(n) using 3 pointers
# Space Complexity: O(1)
'''
Approach:
- If the ith element is 0 then swap the element to the low range.
- Similarly, if the element is 1 then keep it as it is.
- If the element is 2 then swap it with an element in high range.
'''
def sort_array(arr):
    low = 0
    mid = 0
    high = len(arr) - 1
    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

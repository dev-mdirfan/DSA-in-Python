- [Two Pointer](#two-pointer)
  - [Q.1 Pair with target sum](#q1-pair-with-target-sum)
    - [Approach 1 : Brute Force](#approach-1--brute-force)
    - [Code -](#code--)
    - [Approach 2 : Optimize version](#approach-2--optimize-version)
    - [Code -](#code---1)
  - [Q.2 Squaring a sorted array so that it will be sorted array](#q2-squaring-a-sorted-array-so-that-it-will-be-sorted-array)
    - [Approach 1 : Brute Force](#approach-1--brute-force-1)
    - [Approach 2 : Optimized](#approach-2--optimized)
  - [Q.3 Triplet sum to zero (Unique Triplets)](#q3-triplet-sum-to-zero-unique-triplets)
    - [Approach 1. Brute Force](#approach-1-brute-force)
      - [Example of contain duplicate answer](#example-of-contain-duplicate-answer)
      - [Example of not contain duplicate answers](#example-of-not-contain-duplicate-answers)
    - [Approach 2 : Optimized](#approach-2--optimized-1)
  - [Q.4 Count no. of triplets whose sum less than given target](#q4-count-no-of-triplets-whose-sum-less-than-given-target)
    - [Approach 1 : Brute Force](#approach-1--brute-force-2)
    - [Approach 2 : Optimized](#approach-2--optimized-2)
  - [Q.5 You are given an array nums and a range \[a, b\] of triplets whose sum lies in that range \[a, b\]](#q5-you-are-given-an-array-nums-and-a-range-a-b-of-triplets-whose-sum-lies-in-that-range-a-b)
  - [Q.6 `Dutch National Flag` Problem](#q6-dutch-national-flag-problem)
    - [Approach 1: Brute Force](#approach-1-brute-force-1)
    - [Approach 2: Optimized](#approach-2-optimized)
  - [Q.7 Backspace String Compare](#q7-backspace-string-compare)
    - [Approach 1: Brute Force](#approach-1-brute-force-2)
    - [Approach 2: Optimized](#approach-2-optimized-1)
  - [Other Questions Link](#other-questions-link)
- [Advance Mix Topic](#advance-mix-topic)
    - [Note :- Prior Knowledge of](#note---prior-knowledge-of)

## Q.4 Count no. of triplets whose sum less than given target

-

- **Example -**

|-1|4|2|1|3|
|--|--|--|--|--|
|0|1|2|3|4|

- Target = 5

- **Answer :** 4

[-1, 4, 1], [-1, 2, 1], [-1, 2, 3], [-1, 1, 3]

### Approach 1 : Brute Force

- ***Time Complexity :*** O (n<sup>3</sup>)
- ***Space Complexity :*** O (1)

```py
def countTriplet(arr, target):
    count = 0
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1, len(arr)):
                if arr[i] + arr[j] + arr[k] < target:
                    count += 1
    return count

arr = [-1, 4, 2, 1, 3]
target = 5
print(countTriplet(arr, target))
```

### Approach 2 : Optimized

1. Sort the array.

```py
def countTriplet(arr, target):
    arr.sort()
    count = 0
    for i in range(len(arr)-2):
        count += find_pair(arr, arr[i], i+1, target)
    return count

def find_pair(arr, first, start, target):
    count = 0
    end = len(arr)-1
    while start<end:
        if first + arr[start] + arr[end] < target:
            count += (end-start)
            start += 1
        else:
            end -= 1
    return count

arr = [-1, 4, 2, 1, 3]
target = 5
print(countTriplet(arr, target))
```

## Q.5 You are given an array nums and a range [a, b] of triplets whose sum lies in that range [a, b]

| S.No | Question                                                    | Solution | Platform | Related Topics | Difficulty |
| ---- | ----------------------------------------------------------- | -------- | -------- | -------------- | ---------- |
| 1.   | [3Sum Closest](https://leetcode.com/problems/3Sum-Closest/) |          | Leetcode | `Hash Map`     | **M** |

## Q.6 `Dutch National Flag` Problem

| S.No | Question                                                       | Solution | Related Topics | Difficulty |
| ---- | -------------------------------------------------------------- | -------- | -------------- | ---------- |
| 1.   | [Sort an array of 0s, 1s and 2s](https://practice.geeksforgeeks.org/problems/sort-an-array-of-0s-1s-and-2s4231/1) |          |     | **Easy** |
| 2.   | [75. Sort Colors](https://leetcode.com/problems/sort-colors/) |          |     | **Medium** |
| 3.   | [Binary Array Sorting](https://practice.geeksforgeeks.org/problems/binary-array-sorting-1587115620/1) |          |     | **Easy** |

- The problem was proposed by Edsger Dijkstra.
- This problem is also follows as:
  - Given N balls of color red, white or blue arranged in a line in random order. You have to arrange all the balls such that all red coloured balls come first then the white coloured balls and then the blue coloured balls.

| 0 | 0 | 0 | 1 | 1 | 1 | 1 | 2 | 0 | 1 | 1 | 0 | 2 | 1 | 1 | 0 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |

| 0 | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 2 | 2 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |

- If the ith element is 0 then swap the element to the low range.
- Similarly, if the element is 1 then keep it as it is.
- If the element is 2 then swap it with an element in high range.

### Approach 1: Brute Force

- Sort the array
- ***Time Complexity :*** O (nlogn)
- ***Space Complexity :*** O (1)

```py
def dnf(arr):
    arr.sort()
    return arr

arr = [0,2,0,1,2,1,1,1,0,0,0,2,2,1]
print(dnf(arr))
```

### Approach 2: Optimized

- This is `in-place` algorithm
- ***Time Complexity :*** O (n)
- ***Space Complexity :*** O (1)

```py

```

## Q.7 Backspace String Compare

- ***Time Complexity :***
- ***Space Complexity :***

-

### Approach 1: Brute Force

### Approach 2: Optimized

## Other Questions Link

| S.No | Question                                                       | Solution | Related Topics | Difficulty |
| ---- | -------------------------------------------------------------- | -------- | -------------- | ---------- |
| 1.   | [3Sum Closest](https://leetcode.com/problems/two-sum/) |          | `Hash Map`     | **Easy** |
| 2.   | [3Sum Closest](https://leetcode.com/problems/two-sum/) |          | `Hash Map`     |
| 3.   | [3Sum Closest](https://leetcode.com/problems/two-sum/) |          | `Hash Map`     |

# Advance Mix Topic

### Note :- Prior Knowledge of

**[3. Linked List](../README.md/#10-sorting10-sorting)**

| S.No | Question                                                       | Solution | Related Topics |
| ---- | -------------------------------------------------------------- | -------- | -------------- |
| 1.   | [Two Sum (Not sorted)](https://leetcode.com/problems/two-sum/) |          | `Linked List`     |
| 2.   | [Two Sum (Not sorted)](https://leetcode.com/problems/two-sum/) |          | `Hash Map`     |

88. Merge Sorted Array

<https://leetcode.com/problems/sort-transformed-array/>

<https://workat.tech/problem-solving/topics/two-pointers/practice>

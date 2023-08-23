Two pointers is really an easy and effective technique that is typically used for searching pairs in a sorted array.
Given a sorted array A (sorted in ascending order), having N integers, find if there exists any pair of elements $(A[i], A[j])$ such that their sum is equal to $X$.

**Illustration :**

The algorithm basically uses the fact that the input array is sorted. We start the sum of extreme values (smallest and largest) and conditionally move both pointers. We move left pointer `i` when the sum of $A[i]$ and $A[j]$ is less than $X$. We do not miss any pair because the sum is already smaller than $X$. Same logic applies for right pointer $j$.

```cpp
A[] = {10, 20, 35, 50, 75, 80}
X = 70
i = 0
j = 5

A[i] + A[j] = 10 + 80 = 90
Since A[i] + A[j] > X, j--
i = 0
j = 4

A[i] + A[j] = 10 + 75 = 85
Since A[i] + A[j] > X, j--
i = 0
j = 3

A[i] + A[j] = 10 + 50 = 60
Since A[i] + A[j] < X, i++
i = 1
j = 3
m
A[i] + A[j] = 20 + 50 = 70
Thus this signifies that Pair is Found.
```

**Methods:**

Here we will be proposing a two-pointer algorithm by starting off with the naïve approach only in order to showcase the execution of operations going on in both methods and secondary to justify how two-pointer algorithm optimizes code via time complexities across all dynamic programming languages such as C++, Java, Python, and even JavaScript
1. Naïve Approach using loops
2. Optimal approach using two pointer algorithm

**Implementation:**

**Method 1:** Naïve Approach

```python
# Python Program Illustrating Naive Approach to
# Find if There is a Pair in A[0..N-1] with Given Sum

def isPairSum(A, N, X):
	for i in range(N):
		for j in range(N):
			# as equal i and j means same element
			if(i == j):
				continue
			# pair exists
			if (A[i] + A[j] == X):
				return True
			# as the array is sorted
			if (A[i] + A[j] > X):
				break
	# No pair found with given sum
	return 0

# Driver code
arr = [2, 3, 5, 8, 9, 10, 11]
val = 17
print(isPairSum(arr, len(arr), val))
```

**Output**
> 1

**Time Complexity:**  $O(n^2)$.
**Auxiliary Space:** $O(1)$

**Method 2:** Two Pointers Technique

Now let’s see how the two-pointer technique works. We take two pointers, one representing the first element and other representing the last element of the array, and then we add the values kept at both the pointers. If their sum is smaller than X then we shift the left pointer to right or if their sum is greater than X then we shift the right pointer to left, in order to get closer to the sum. We keep moving the pointers until we get the sum as X.

```python
# Find if There is a Pair in A[0..N-1] with Given Sum
# Using Two-pointers Technique

def isPairSum(A, N, X):
	# represents first pointer
	i = 0
	# represents second pointer
	j = N - 1
	
	while(i < j):
		# If we find a pair
		if (A[i] + A[j] == X):
			return True
		# If sum of elements at current pointers is less, we move towards
		# higher values by doing i += 1
		elif(A[i] + A[j] < X):
			i += 1
		# If sum of elements at current pointers is more, we move towards
		# lower values by doing j -= 1
		else:
			j -= 1
	return 0

arr = [2, 3, 5, 8, 9, 10, 11]
# Given Array is may not be sorted so sort function used.
# value to search
val = 17
print(isPairSum(arr, len(arr), val))
```

**Time Complexity:**  O(n log n) (As sort function is used)

**Auxiliary Space:** O(1), since no extra space has been taken.






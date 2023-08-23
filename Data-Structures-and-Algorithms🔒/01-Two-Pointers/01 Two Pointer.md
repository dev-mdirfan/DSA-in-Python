## Session 1

> September 06 2022

- **Sorted** (Array/Linked List) will be given.
- You will need to calculate some **specific numbers** that **matches** some value.
- The set of elements could be a pair, a triplet or even a subarray.

### 1. Pair with Target Sum
---

If you already know the topic get let you try first.
```ad-important
**Solve On:** [167. Two Sum II](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

**Given:** Input array is sorted

**Difficulty:** Easy

**Additional Topic:** ?
```

> **Given:** An array of sorted numbers. And a target sum.
> 
> **Find:** A pair of indices in the array whose sum is equal to the given target.


```yaml
Input: [2, 4, 7, 8, 12, 14]
Target Sum: 13
Output: [1, 4]
```

| 2   | 4   | 7   | 8   | 9   | 12  | 14  |
| --- | --- | --- | --- | --- | --- | --- |
| 0   | 1   | 2   | 3   | 4   | 5   | 6   |

#### Approach 1: Brute Force

- Here the length of the array is n = **7**.
- Iterating for each elements (pointed by first pointer) we search second element in remaining elements (pointed by second pointer)
-  For First number 2: (2 + 4), (2 + 7), (2 + 8), ( 2 + 9), (2 + 12) (2 + 14) possible sum (6 = n - 1).
- For First number 4: (5 = n - 2) possible sum and so on.
- Time Analysis: $$ Total Possible Sum =  6 + 5 + 4 + 3 + 2 + 1 $$
- For n: $$ Total Possible Sum = (n -1) + (n - 2) + (n - 3) + .... + 2 + 1 $$
- Sum of the first n natural no: $$ = \frac{n(n + 1) }{2} $$
- Sum of the first (n - 1) no: $$ = \frac{n(n - 1)}{2} = \frac{n^2}{2} - \frac{n}{2} $$
- So, $$ Time Complexity: O(n^2) $$ and $$ Space Complexity: O(1) $$
**Code:**

```python
# T.C: O(n^2)
def solve(arr,target):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return [i, j]
    return [-1, -1]

arr = [2, 4, 8, 7, 9, 12, 14]
target = 13
print(solve(arr, target))
```

#### Approach 2: Optimized Version


```ad-hint
**Ask Yourself:** Why the array is sorted?
```

| 2   | 4   | 7   | 8   | 9   | 12  | 14  |
| --- | --- | --- | --- | --- | --- | --- |
| 0   | 1   | 2   | 3   | 4   | 5   | 6   |

- An efficient way would be to start with one pointer in the beginning and another pointer at the end.
- At every step, we will see if the numbers pointed by the two pointers add up to the target sum. If they do not, we will do one of two things:
	- If the sum of the two numbers pointed by the two pointers is greater than the target sum, this means that we need a pair with a smaller sum. We have to add smaller value for that we have to decrement end pointer index.
	- If the sum of the two numbers pointed by the two pointers is less than the target sum, this means that we need a pair with a greater sum. We have to add greater value for that we have to increment start pointer.

$$ Time Complexity: O(n) $$
$$ Space Complexity: O(1) $$
  

![](media/Two-Pointers.png)

**Code:**
```python
# T.C: O(n)
def pairSum(arr,target):
    left = 0
    right = len(arr)-1
    while left < right:
        Sum = arr[left] + arr[right]
        if Sum == target:
            return [left,right]
        elif Sum < target:
            left += 1
        else:
            right -= 1
    return [-1, -1]

arr = [1, 3, 5, 6, 8, 9]
target = 11
print(pairSum(arr, target))
```

### 2. Squaring a Sorted Arrays

If you already know the topic get let you try first.
```ad-important
**Solve On:** [977. Squares of a Sorted Array](https://leetcode.com/problems/squares-of-a-sorted-array/)

**Given:** Input array is sorted

**Difficulty:** Easy

**Additional Topic:** ?
```

> **Given:** You are given a sorted array of whole numbers.
> 
> **Find:** calculate their squares and the array should be in sorted.

```yaml
Input: [2, 4, 7, 8, 9, 12, 14]
Output: [4, 16, 49, 64, 81, 144, 196]
```

```yaml
Input: [-5, -4, -2, 0, 1, 3, 4]
Output: [0, 1, 4, 9, 16, 16, 25]
```

#### Approach 1: Brute Force

- Simply calculate squares and store values into the another `answer` array.
- And then sort the array.

$$ Time Complexity: O(n \log_{10}n) For Sorting $$
$$ Space Complexity: O(n) $$

```python
def squareArr(arr):
	ans = []
	for i in arr:
		ans.append(i*i)
	return sorted(ans)

arr = [-5, -4, -1, 0, 2, 3, 4]
print(squareArr(arr))
```

#### Approach 2: Optimized

- let us take two pointer at start and end of the array.

$$ Time Complexity: O(n) $$
$$ Space Complexity: O(n) $$

```python
def square(arr):
	left,right = 0, len(arr)-1
	index = len(arr)-1
	ans = [0]*len(arr)
	while left<=right:
		lsquare = arr[left]**2
		rsquare = arr[right]**2
		if lsquare > rsquare:
			ans[index] = lsquare
			left += 1
		else:
			ans[index] = rsquare
			right -= 1
		index -= 1
	return ans

arr = [-5, -4, -2, 0, 1, 3, 4]
print(square(arr))
```

**OR**

```python
def squareArr(arr):
	ans = []
	left, right = 0, len(arr)-1
	while left<=right:
		l = arr[left]*arr[left]
		r = arr[right]*arr[right]
		if l>r:
			ans.insert(0,l)
			left += 1
		else:
			ans.insert(0,r)
			right -= 1
	return ans

arr = [-5, -4, -1, 0, 2, 3, 4]
print(squareArr(arr))
```

## Session 2

> September 08 2022

### 3. Triplet Sum to Zero (Unique Triplets)

If you already know the topic get let you try first.
```ad-important
1. **Solve On:** [Find triplets with zero sum](https://practice.geeksforgeeks.org/problems/find-triplets-with-zero-sum/1)
	
	**Platform:** GFG
	
	**Difficulty:** Easy
	
	**Additional Topic:** `HashMap`
2. **Solve On:** [15. 3Sum](https://leetcode.com/problems/3sum/)
	
	**Platform:** Leetcode
	
	**Difficulty:** Medium
	
	**Additional Topic:** `HashMap`
3. **Solve On:** [3Sum Closest](https://leetcode.com/problems/3Sum-Closest/)
	
	**Platform:** Leetcode
	
	**Difficulty:** Medium
	
	**Additional Topic:** `HashMap`
```

> **Given:** An unsorted array.
> **Find:** Find all unique triplets in the array which gives the sum of zero.
> The solution set must contain unique triplets.


```yaml
Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
```

|-3|0|1|2|-1|1|-2|
|--|--|--|--|--|--|--|
|0|1|2|3|4|5|6|

![Triplet Sum to Zero](media/triplet-with-zero-sum.png)

```ad-note
For Solution you must think first on pen and paper.
```

#### Approach 1: Brute Force

| Insert Figure to Illustrate the brute force
1.
2.
3.
4.
5.
6.
7.
```python
def tripletZero(arr):
	n = len(arr)
	ans = set()
	for i in range(n-2):
		for j in range(i+1,n-1):
			for k in range(j+1,n):
				if arr[i] + arr[j] + arr[k] == 0:
					ans.add((arr[i], arr[j], arr[k]))
	return ans
	
arr = [-3, 0, 1, 2, -1, 1, -2]
print(tripletZero(arr))
```
**Output:** {(0, -1, 1), (-3, 1, 2), (1, 1, -2), (0, 1, -1), (0, 2, -2), (-3, 2, 1)}

```ad-warning
Here, the solution not contains unique sum.
```

**Complexity Analysis:**
$$ Time Complexity : O (n^3) $$ $$ Space Complexity: O (1), approx $$

#### Approach 2: Optimized

1. First sort the array.
2. Treat the third element (negative of original) as a target of remaining two element $(x + y = - z)$.

|-3|0|-2|1|-1|2|1|-3|2|
|--|--|--|--|--|--|--|--|--|
|0|1|2|3|4|5|6|7|8|

```python
def tripletZero(arr):
	triplets = []
	arr.sort()
	for i in range(len(arr)):
		target = -arr[i]
		if i>0 and arr[i]==arr[i-1]:
			continue
		find_pair(arr,i+1,target,triplets)
	return triplets

def find_pair(arr, left,target, triplets):
	right = len(arr)-1
	while left<right:
		arrsum = arr[left] + arr[right]
		if arrsum==target:
			triplets.append([-target, arr[left], arr[right]])
			left += 1
			right -= 1
			# To remove duplicate pair
			while left<right and arr[left]==arr[left-1]:
				left += 1
			while left<right and arr[right]==arr[right+1]:
				right -= 1
		elif arrsum< target:
			left += 1
		else:
			right -= 1

arr = [-3, -3, 0, 1, 2, 2, -1, 1, -2, -2]
print(tripletZero(arr))
```

- ***Time Complexity :*** $O (n^2)$
- ***Space Complexity :*** $O (n)$
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
.
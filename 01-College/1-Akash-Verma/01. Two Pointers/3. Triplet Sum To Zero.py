### 3. Triplet Sum to Zero (Unique Triplets)

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


# or using two pointer approach
# Time: O(n^2) and Space: O(n) for storing triplets
def tripletZero(arr):
	triplets = []
	arr.sort()
	for i in range(len(arr)):
		target = -arr[i]	# To find pair sum to target value arr[i] + arr[j] + arr[k] = 0
		if i>0 and arr[i]==arr[i-1]:	# To remove duplicate triplets
			continue
		find_pair(arr, i+1, target, triplets)
	return triplets

def find_pair(arr, left,target, triplets):
	right = len(arr)-1
	while left<right:
		arrsum = arr[left] + arr[right]
		if arrsum == target:
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

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

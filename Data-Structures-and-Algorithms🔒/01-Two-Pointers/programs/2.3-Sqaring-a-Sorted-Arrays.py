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
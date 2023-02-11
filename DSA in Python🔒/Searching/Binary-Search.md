# Binary Search

- **Condition -** Elements must be `sorted`
- Array = [8, 10, 12, 21, 27, 34, 42], key = 27
<pre>
start = 0
end = len(array)

while start<=end:
    mid = (start+end)/2
    if array[mid]==key:
        return mid
    elif array[mid]>key:
        end = mid-1
    else:
        start = mid+1
</pre>

- **Time Complexity -** O(log n)

| S.No | Questions    | Solutions      | Type | Tags   |
| ---- | ------------ | -------------- | ---- | ------ |
| 1.   | [69. Sqrt]() | [3-solution]() | Easy | `math` |

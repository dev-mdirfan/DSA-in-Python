# print stars in given array
arr = [2, 3, 0, 4, 5, 10]
n = len(arr)
counter = [0] * n
mx = max(arr)
for i in range(mx):
    for j in range(n):
        if counter[j] < arr[j]:
            print("*", end=" ")
            counter[j] += 1
        else:
            print(' ', end=" ")
    print()

# using max
arr = [2, 3, 0, 4, 5, 10]
n = max(arr)
for i in range(n):
    for j in range(len(arr)):
        if arr[j]:
            print("*", end=" ")
            arr[j] -= 1
        else:
            print(' ', end=" ")
    print()

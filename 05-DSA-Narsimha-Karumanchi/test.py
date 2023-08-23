n = int(input())
index = int(input())
m = int(input())
arr = list(map(int, input().split()))

sum1 = 0
sum2 = 0

for i in range(len(arr[: index + 1])):
    sum1 += arr[i]
for i in range(len(arr[index : ])):
    sum2 += arr[i]

print(max(sum1, sum2))


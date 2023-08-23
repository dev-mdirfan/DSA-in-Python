arr = [3, 5, 2, 1, 4, 7, 9, 6, 8]

# ans = []
# n = len(arr)
# for i in range(n):
#     for j in range(i+1, n):
#         if arr[j] > arr[i]:
#             ans.append(arr[j])
#             break
#     else:
#         ans.append(-1)
# print(ans)


# # m2
st = [-1]
ans = []
start = len(arr) -1
while start>= 0:
    while len(st) > 0 and arr[start] > st[-1]:
        st.pop()
    if len(st) == 0:
        ans.append(-1)
    elif arr[start] < st[-1]:
        ans.append(st[-1])
    st.append(arr[start])
    start -= 1
print(ans[::-1])


n = 5
counter = 1
for i in range(n):
    for j in range(n):
        if j < n-i:
            print(counter, end=" ")
            counter += 1
        else:
            print(" ", end=" ")
    print()
# count odd factors of a number

def count_odd_factors(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0 and i % 2 != 0:
            count += 1
    return count

# test the function
print(count_odd_factors(30))  # 3
print(count_odd_factors(15))  # 2
print(count_odd_factors(16))  # 0
print(count_odd_factors(1))  # 1
print(count_odd_factors(0))  # 0

# Time complexity: O(n)

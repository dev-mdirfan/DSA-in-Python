# print recursion function
# With base case
# Finite times
count = 0
class solution:
    def recursion(self):
        global count
        if count == 3:
            return
        print(count)
        count += 1
        self.recursion()
    def __init__(self):
        self.recursion()

test = solution()
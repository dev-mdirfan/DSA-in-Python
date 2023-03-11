# print recursion function
# Without Base Condition
# Infinite times calls
class solution:
    def recursion(self):
        print(1)
        self.recursion()
    
    def __init__(self):
        self.recursion()

test = solution()
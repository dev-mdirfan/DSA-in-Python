# Frog Jump
# BFS without queue
class Solution:
    def canCross(self, stones: List[int]) -> bool:
        graph = dict()
        
        # creating dict of set
        for stone in stones:
            graph[stone] = set()
        
        graph[0].add(1)
        
        for currPosition in stones:
            jumps = graph[currPosition]
            for jump in jumps:
                newPosition = currPosition + jump
                # If reach end return True
                if newPosition == stones[-1]:
                    return True
                # if stone position exits then add next jumps
                if newPosition in graph:
                    if jump - 1 > 0:
                        graph[newPosition].add(jump - 1)
                    graph[newPosition].add(jump)
                    graph[newPosition].add(jump + 1)
        return False

# Recursion
# Pure Recursion: TLE
class Solution: 
    def solve(self, currentPosition, previousJump):
        # Second Invalid Condition
        if previousJump <= 0:
            return False
        # Third Invalid Condition
        if currentPosition not in self.stones:
            return False
        # Valid Condition Only in reaching end of the stones
        if currentPosition == self.stones[-1]:
            return True
        # Recursion
        return self.solve(currentPosition + previousJump - 1, previousJump - 1) or self.solve(currentPosition + previousJump, previousJump) or self.solve(currentPosition + previousJump + 1, previousJump + 1)
    def canCross(self, stones: List[int]) -> bool:
        self.stones = stones
        # First Invalid Condition
        if stones[1] != 1:
            return False
        return self.solve(1, 1)

class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        cache = {}

        def dfs(x, y):
            if (x, y) in cache:
                return cache[(x, y)]
            if x + y == 0:
                return 0
            
            if x + y == 2:
                return 2
            
            else:
                ans = min(dfs(abs(x - 1), abs(y - 2)), dfs(abs(x - 2), abs(y - 1))) + 1
                cache[(x, y)] = ans
                return ans
        
        return dfs(abs(x),abs(y))
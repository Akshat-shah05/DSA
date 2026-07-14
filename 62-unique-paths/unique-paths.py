class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # number of ways to get to square (r, c) is 
            # number of ways to get to square (r, c - 1) + (r - 1, c)
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[1][1] = 1

        for r in range(1, m + 1):
            for c in range(1, n + 1):    
                if (r, c) == (1, 1):
                    continue
                
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        
        return dp[m][n]


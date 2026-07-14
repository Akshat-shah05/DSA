class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        if n == 2:
            return 2
        
        prev1 = 1
        prev2 = 2

        # dp[i] is # of distinct ways to get to stair i
        # dp[i] = dp[i - 1] + dp[i - 2]

        for i in range(3, n + 1):
            tmp = prev2
            prev2 = tmp + prev1
            prev1 = tmp
        
        return prev2
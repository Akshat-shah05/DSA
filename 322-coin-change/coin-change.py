class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            if coin < amount:
                dp[coin] = 1

        for i in range(amount + 1):
            min_val = float('inf')
            for coin in coins:
                prev = i - coin
                if i - coin >= 0:
                    min_val = min(min_val, dp[prev])
            
            dp[i] = min(dp[i], min_val + 1) 
        
        return dp[amount] if dp[amount] != float('inf') else -1


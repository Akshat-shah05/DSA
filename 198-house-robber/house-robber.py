class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        # let dp[i] represent the maximum amount of money you can make from houses 0 to i
        #   dp[0] = 0 // robbing no houses
        #   dp[1] = 1 // robbing 1 house
        #   dp[2] = max(dp[0], dp[1])
        #   dp[3] = max(dp[1] + nums[3], dp[2])
        n = len(nums)
        if n == 0:
            return 0
        
        if n == 1:
            return nums[0]

        dp = [0] * (n + 1)
        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])

        for i in range(3, n + 1):
            dp[i] = max(dp[i - 2] + nums[i - 1], dp[i - 1])
        
        return dp[n]


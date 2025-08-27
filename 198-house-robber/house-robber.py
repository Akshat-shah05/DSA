class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        memo = {}
        def dp(i):
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = max(dp(i + 2) + nums[i], dp(i + 1))
            return memo[i]

        return dp(0)
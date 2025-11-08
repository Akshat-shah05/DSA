class Solution:
    def rob(self, nums: List[int]) -> int:
        # Smallest Case
            # If one house --> max value is nums[0]
            # If two houses --> max value is max(nums[1], nums[0])
            # IF > 2 houses 
                # For any house i with value v, its max value is 
                    #  max(v + (max value for house i - 2), (max value for house i - 1))
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        dp = [0] * (len(nums) + 1)
        dp[1] = nums[0]
        dp[2] = max(nums[0], nums[1])

        for i in range(3, len(nums) + 1):
            dp[i] = max(dp[i - 1], nums[i - 1] + dp[i - 2])
        
        return dp[-1]

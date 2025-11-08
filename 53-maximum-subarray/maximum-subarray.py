class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        curSum = 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            
            curSum += num
            ans = max(ans, curSum)
        
        return ans
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        if len(nums) == 1:
            return nums[0]
            
        return max(self.robHelper(nums[1:]), self.robHelper(nums[:-1]))
    
    def robHelper(self, nums):
        prev1, prev2 = 0, 0
        for num in nums:
            temp = max(prev2 + num, prev1)
            prev2 = prev1
            prev1 = temp
        
        return prev1
        
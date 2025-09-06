class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2, prev1 = 0, 0

        for num in nums:
            temp = max(num + prev2, prev1)
            prev2 = prev1
            prev1 = temp
        
        return prev1
        
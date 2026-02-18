class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
        
        mid = n//2
        
        left = self.maxSubArray(nums[:mid])
        right = self.maxSubArray(nums[mid:])
    
        cross = self.maxLower(nums[:mid]) + self.maxHigher(nums[mid:])

        return max(left, right, cross)
    
    def maxLower(self, A):
        cur = 0
        best = float("-inf")
        i = len(A)
        for i in range(len(A) - 1, -1, -1):
            cur += A[i]
            best = max(best, cur)
        
        return best
    
    def maxHigher(self, A):
        cur = 0
        best = float("-inf")
        for i in range(len(A)):
            cur += A[i]
            best = max(best, cur)

        return best

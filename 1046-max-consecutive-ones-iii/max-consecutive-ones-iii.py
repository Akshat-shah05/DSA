class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l = 0
        numZeroes = 0
        ans = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                numZeroes += 1
            
            while numZeroes > k:
                if nums[l] == 0:
                    numZeroes -= 1
                
                l += 1
            
            ans = max(ans, r - l + 1)
    
        return ans

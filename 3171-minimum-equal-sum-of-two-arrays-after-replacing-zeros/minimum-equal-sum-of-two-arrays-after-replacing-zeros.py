class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1sum, nums2sum = self.modifiedSum(nums1), self.modifiedSum(nums2)
        if nums1sum == nums2sum:
            return nums1sum

        if nums1sum > nums2sum:
            if nums2.count(0) == 0:
                return -1
            
            return nums1sum
        
        if nums1sum < nums2sum:
            if nums1.count(0) == 0:
                return -1
            
            return nums2sum
    
    def modifiedSum(self, nums):
        ans = 0
        for num in nums:
            ans += num if num != 0 else 1
        
        return ans
            
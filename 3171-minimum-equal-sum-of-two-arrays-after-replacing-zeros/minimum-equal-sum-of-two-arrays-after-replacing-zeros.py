class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1sum = 0
        nums2sum = 0
        for num in nums1:
            if num == 0:
                nums1sum += 1
            
            nums1sum += num
        
        for num in nums2:
            if num == 0:
                nums2sum += 1
            
            nums2sum += num
        
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
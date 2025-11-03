class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        n1s, n2s = 0, 0

        for num in nums1:
            n1s += num if num != 0 else 1
        
        for num in nums2:
            n2s += num if num != 0 else 1
        
        if n1s > n2s:
            if nums2.count(0) == 0:
                return -1
            
            return n1s
        
        if n2s > n1s:
            if nums1.count(0) == 0:
                return -1
            
            return n2s
        
        return n1s
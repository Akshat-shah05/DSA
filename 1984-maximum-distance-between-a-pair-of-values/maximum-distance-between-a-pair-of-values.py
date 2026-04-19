class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        p1, p2 = 0, 0
        maxPair = float('-inf')

        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] <= nums2[p2]:
                maxPair = max(maxPair, p2 - p1)
                p2 += 1

            elif nums1[p1] > nums2[p2]:
                if p1 < p2:
                    p1 += 1
                else:
                    p2 += 1
        
        return 0 if maxPair == float('-inf') else maxPair

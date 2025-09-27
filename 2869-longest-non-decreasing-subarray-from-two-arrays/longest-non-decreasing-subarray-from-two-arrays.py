class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        # check if nums1[i] >= nums1[i - 1] and nums1[i] >= nums2[i - 1]
        # check if nums2[i] >= nums2[i - 1] and nums2[i] >= nums1[i - 1]

        # dp[i][0] --> would represent longest nondecreasing subarray, given you choose nums1[i]
        # dp[i][1] --> would represent longest nondecreasing subarray, given you choose nums2[i]

        dp = [[1, 1] for _ in range(len(nums1))]
        ans = 1
        a = 1
        b = 1

        for i in range(1, len(nums1)):
            na, nb = 1, 1

            if nums1[i] >= nums1[i - 1]:
                na = a + 1
            if nums1[i] >= nums2[i - 1]:
                na = max(na, b + 1)
            if nums2[i] >= nums2[i - 1]:
                nb = b + 1
            if nums2[i] >= nums1[i - 1]:
                nb = max(a + 1, nb)
            
            a, b = na, nb
            ans = max(ans, a, b)
        
        return ans
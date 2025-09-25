class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        # dp[i][j] represents the longest non-decreasing ending with nums1[i] and nums2[i]
        n = len(nums1)
        dp = [[1, 1] for _ in range(len(nums1))]
        ans = 1
        for i in range(1, n):
            dp[i][0] = 1
            dp[i][1] = 1

            if nums1[i] >= nums1[i - 1]:
                dp[i][0] = max(dp[i][0], dp[i - 1][0] + 1)
            if nums1[i] >= nums2[i - 1]:
                dp[i][0] = max(dp[i][0], dp[i - 1][1] + 1)
            
            if nums2[i] >= nums2[i - 1]:
                dp[i][1] = max(dp[i][1], dp[i - 1][1] + 1)
            if nums2[i] >= nums1[i - 1]:
                dp[i][1] = max(dp[i][1], dp[i - 1][0] + 1)
            
            ans = max(ans, dp[i][0], dp[i][1])
        
        return ans
class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        # check if nums1[i] >= nums1[i - 1] and nums1[i] >= nums2[i - 1]
        # check if nums2[i] >= nums2[i - 1] and nums2[i] >= nums1[i - 1]

        # dp[i][0] --> would represent longest nondecreasing subarray, given you choose nums1[i]
        # dp[i][1] --> would represent longest nondecreasing subarray, given you choose nums2[i]

        dp = [[1, 1] for _ in range(len(nums1))]
        ans = 1

        for i in range(1, len(nums1)):
            if nums1[i] >= nums1[i - 1]:
                dp[i][0] = dp[i - 1][0] + 1
            if nums1[i] >= nums2[i - 1]:
                dp[i][0] = max(dp[i][0], dp[i - 1][1] + 1)
            if nums2[i] >= nums2[i - 1]:
                dp[i][1] = dp[i - 1][1] + 1
            if nums2[i] >= nums1[i - 1]:
                dp[i][1] = max(dp[i - 1][0] + 1, dp[i][1])
            
            ans = max(ans, dp[i][0], dp[i][1])
        
        return ans
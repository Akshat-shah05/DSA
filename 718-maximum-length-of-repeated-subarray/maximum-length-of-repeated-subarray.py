class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # let dp[i][j] be the length of the longest common prefix of the suffixes A[i:], B[i:]
        # then if A[i] == B[j], we know that dp[i][j] = dp[i + 1][j + 1] + 1
        A, B = nums1, nums2

        dp = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]

        for i in range(len(A) - 1, -1, -1):
            for j in range(len(B) - 1, -1, -1):
                if A[i] == B[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
        
        return max(max(row) for row in dp)

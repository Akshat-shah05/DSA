class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # DP[i][j] will represent the maximum sidelength of a square whose bottom corner is (i, j)
        # DP[i][j] = min(DP[i - 1][j], DP[i - 1][j - 1], DP[i][j - 1]) + 1

        rows, cols = len(matrix), len(matrix[0])
        dp = [[0] * (cols + 1) for _ in range(rows + 1)]

        maxsqlen = 0

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                if matrix[i - 1][j - 1] == "1":
                    dp[i][j] = min (
                        dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]
                    ) + 1
                    maxsqlen = max(maxsqlen, dp[i][j])
        
        return maxsqlen**2

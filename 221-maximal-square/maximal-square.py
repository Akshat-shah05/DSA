class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # let dp[i][j] represent sidelength of max square with bottom right corner (i, j)
        # dp[i][j] += min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1])
        ROWS, COLS = len(matrix), len(matrix[0])
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        max_side = 0

        for r in range(1, ROWS + 1):
            for c in range(1, COLS + 1):
                if matrix[r - 1][c - 1] == "1":
                    dp[r][c] = 1 + min(
                        dp[r-1][c-1],
                        dp[r][c-1],
                        dp[r-1][c]
                    )
                
                max_side = max(max_side, dp[r][c])

        return max_side ** 2
                
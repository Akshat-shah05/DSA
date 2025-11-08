class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])

        for r in range(1, rows):
            prev = matrix[r - 1]
            for c in range(cols):
                matrix[r][c] += min(prev[max(0, c - 1): min(cols, c + 2)]) 

        return min(matrix[-1])
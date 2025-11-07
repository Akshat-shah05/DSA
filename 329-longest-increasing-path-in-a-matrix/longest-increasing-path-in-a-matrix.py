class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        cache = {}
        maxLength = 0

        def dfs(r, c):
            if not (0 <= r < rows) or not (0 <= c < cols):
                return 0

            if (r, c) in cache:
                return cache[(r, c)]

            ans = 1

            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if 0 <= newR < rows and 0 <= newC < cols and matrix[newR][newC] > matrix[r][c]:
                   ans = max(ans, dfs(newR, newC) + 1)

            cache[(r, c)] = ans
            return ans
        
        for r in range(rows):
            for c in range(cols):
                maxLength = max(maxLength, dfs(r, c))
        
        return maxLength

                

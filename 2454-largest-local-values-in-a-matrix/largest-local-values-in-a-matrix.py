class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        res = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(1, n - 1):
            for j in range(1, n - 1):
                for dx, dy in [(-1, -1), (-1, 0), (1, 1), (1, 0), (1, -1), (0, 1), (-1, 1), (0, -1), (0, 0)]:
                    res[i - 1][j - 1] = max(res[i - 1][j - 1], grid[i + dx][j + dy])
        
        return res

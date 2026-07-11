class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        seen = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in seen or grid[r][c] == 0:
                return 0
            
            seen.add((r, c))
            ans = 1
            for dr, dc in directions:
                ans += dfs(r + dr, c + dc)
            
            return ans
        
        max_area = 0
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in seen and grid[r][c] == 1:
                    ans = dfs(r, c)
                    max_area = max(max_area, ans)
        
        return max_area
                
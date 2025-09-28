class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        islands = 0

        def dfs(r, c):
            if grid[r][c] == "0":
                return
            
            grid[r][c] = "0"
            
            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] == "1":
                    dfs(newR, newC)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)
        
        return islands
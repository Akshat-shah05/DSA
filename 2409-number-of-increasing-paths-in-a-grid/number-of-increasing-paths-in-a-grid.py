class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        MOD = 10**9 + 7
        rows, cols = len(grid), len(grid[0])
        total = 0
        cache = {}
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def dfs(r, c):
            if (r, c) in cache:
                return cache[(r, c)]
            
            ans = 1

            for dr, dc in directions:
                newR, newC = r + dr, c + dc
                if 0 <= newR < rows and 0 <= newC < cols and grid[newR][newC] > grid[r][c]:
                    ans += dfs(newR, newC)
            
            ans %= MOD
            cache[(r, c)] = ans
            return ans
        
        for r in range(rows):
            for c in range(cols):
                total += dfs(r, c)
        
        return total % MOD

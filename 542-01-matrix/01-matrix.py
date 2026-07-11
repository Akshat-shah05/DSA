class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        grid = [row[:] for row in mat]
        m, n = len(grid), len(grid[0])
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        
        q = deque()
        seen = set()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    q.append((r, c, 0))
                    seen.add((r, c))

        while q:
            r, c, dist = q.popleft()
            grid[r][c] = dist

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if valid(new_r, new_c) and (new_r, new_c) not in seen:
                    seen.add((new_r, new_c))
                    if grid[new_r][new_c] == 0:
                        q.append((new_r, new_c, dist))
                    
                    else:
                        q.append((new_r, new_c, dist + 1))
        
        return grid



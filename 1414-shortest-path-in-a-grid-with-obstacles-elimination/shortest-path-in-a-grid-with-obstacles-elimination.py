class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1: return 0
        if k >= m + n - 2:     return m + n - 2  # Manhattan shortcut

        q = deque([(0, 0, k, 0)])     # r, c, rem, steps
        seen = {(0, 0, k)}
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            pass

        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        while q:
            r, c, rem, steps = q.popleft()
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < m and 0 <= nc < n:
                    nrem = rem - grid[nr][nc]
                    if nrem < 0: 
                        continue
                    if nr == m-1 and nc == n-1:
                        return steps + 1
                    state = (nr, nc, nrem)
                    if state not in seen:
                        seen.add(state)
                        q.append((nr, nc, nrem, steps+1))
        return -1

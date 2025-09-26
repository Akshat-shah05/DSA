class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        minutes, fresh = 0, 0
        directions = [(0, -1), (1, 0), (-1, 0), (0, 1)]

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1
        
        while q and fresh > 0:
            r, c, minutes = q.popleft()

            for dy, dx in directions:
                if 0 <= r + dy < ROWS and 0 <= c + dx < COLS and grid[r + dy][c + dx] == 1:
                    q.append((r + dy, c + dx, minutes + 1))
                    grid[r + dy][c + dx] = 2
                    fresh -= 1
                    if fresh == 0:
                        return minutes + 1
            
        return minutes if fresh == 0 else -1
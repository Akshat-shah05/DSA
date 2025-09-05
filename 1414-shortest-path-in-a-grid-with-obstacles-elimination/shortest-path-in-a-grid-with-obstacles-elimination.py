class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque([(0, 0, k, 0)])
        
        best = [[-1] * cols for _ in range(rows)]
        best[0][0] = k

        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]

        if rows == cols == 1:
            return 0

        while q:
            row, col, rem, steps = q.popleft()

            for dr, dc in directions:
                newR, newC = row + dr, col + dc

                if 0 <= newR < rows and 0 <= newC < cols:
                    nrem = rem - grid[newR][newC]
                    if nrem < 0:
                        continue
                    
                    if (newR, newC) == (rows - 1, cols - 1):
                        return steps + 1
                            
                    if nrem > best[newR][newC]:
                        best[newR][newC] = nrem
                        q.append((newR, newC, nrem, steps + 1))
        
        return -1
                    





        
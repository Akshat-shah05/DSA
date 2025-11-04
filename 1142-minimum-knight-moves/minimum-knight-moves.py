class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        directions = [(1, 2), (1, -2), (2, 1), (-2, 1), (-1, 2), (-1, -2), (-2, -1), (2, -1)]
        steps = 0
        q = deque([(0, 0)])
        visited = set([(0, 0)])

        while q:
            for _ in range(len(q)):
                curX, curY = q.popleft()
                if (curX, curY) == (x, y):
                    return steps

                for dx, dy in directions:
                    newX, newY = curX + dx, curY + dy
                    if (newX, newY) in visited:
                        continue
                    
                    visited.add((newX, newY))
                    q.append((newX, newY))
                
            steps += 1
        
        return steps
            

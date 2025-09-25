class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        offsets = [(1, 2), (1, -2), (2, 1), (2, -1), (-1, 2), (-1, -2), (-2, 1), (-2, -1)]

        visited = set([(0, 0)])
        q = deque([(0, 0, 0)])

        while q:
            currX, currY, steps = q.popleft()
            if (currX, currY) == (x, y):
                return steps
            
            for dx, dy in offsets:
                newX, newY = currX + dx, currY + dy
                if (newX, newY) not in visited:
                    visited.add((newX, newY))
                    q.append((newX, newY, steps + 1))
        
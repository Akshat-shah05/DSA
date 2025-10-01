class Solution:
    def numSquares(self, n: int) -> int:
        squares = [i * i for i in range(1, math.isqrt(n) + 1)]
        q = deque([n])
        visited = set([n])
        steps = 0

        while q:
            steps += 1
            for _ in range(len(q)):
                num = q.popleft()
                for square in squares:
                    newNum = num - square
                    if newNum == 0:
                        return steps
                    
                    if newNum < 0:
                        break
                    
                    if newNum not in visited:
                        visited.add(newNum)
                        q.append(newNum)
                        





        

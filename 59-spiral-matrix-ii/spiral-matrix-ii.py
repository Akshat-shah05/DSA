class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        counter = 1
        l, r, t, b = 0, n, 0, n

        while True:
            for i in range(l, r):
                matrix[t][i] = counter
                counter += 1
            
            t += 1
            if t == b:
                break
            
            for i in range(t, b):
                matrix[i][r - 1] = counter
                counter += 1
            
            r -= 1
            if r == l:
                break
            
            for i in range(r - 1, l - 1, -1):
                matrix[b - 1][i] = counter
                counter += 1
            
            b -= 1
            if b == t:
                break
            
            for i in range(b - 1, t - 1, - 1):
                matrix[i][l] = counter
                counter += 1
            
            l += 1
            if l == r:
                break
        
        return matrix
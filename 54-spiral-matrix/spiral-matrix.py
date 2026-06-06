class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        ROWS, COLS = len(matrix), len(matrix[0])
        t, b, l, r = 0, ROWS, 0, COLS

        while True:
            for i in range(l, r):
                ans.append(matrix[t][i])
            
            t += 1
            if t == b:
                break
            
            for i in range(t, b):
                ans.append(matrix[i][r - 1])
            
            r -= 1
            if r == l:
                break
            
            for i in range(r - 1, l - 1, -1):
                ans.append(matrix[b - 1][i])
            
            b -= 1
            if b == t:
                break
            
            for i in range(b - 1, t - 1, -1):
                ans.append(matrix[i][l])
            
            l += 1
            if l == r:
                break
            
        return ans
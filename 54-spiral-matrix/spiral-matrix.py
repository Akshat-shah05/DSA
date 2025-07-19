class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS, COLS = len(matrix), len(matrix[0])
        totalElems = ROWS * COLS
        l, r, u, d = 0, COLS, 0, ROWS

        spiral = []
        numElems = 0
        while numElems < totalElems:
            # Go right
            for i in range(l, r):
                spiral.append(matrix[u][i])
                numElems += 1
            u += 1

            # Go Down
            for i in range(u, d):
                spiral.append(matrix[i][r - 1])
                numElems += 1
            r -= 1
            
            if numElems >= totalElems:
                break

            # Go Left
            for i in range(r - 1, l - 1, -1):
                spiral.append(matrix[d - 1][i])
                numElems += 1
            d -= 1
            
            if numElems >= totalElems:
                break

            # Go Up
            for i in range(d - 1, u - 1, -1):
                spiral.append(matrix[i][l])
                numElems += 1
            l += 1

        return spiral
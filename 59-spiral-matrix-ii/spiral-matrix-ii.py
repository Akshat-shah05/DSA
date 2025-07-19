class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        ROWS, COLS = n, n
        totalElems = ROWS * COLS
        l, r, u, d = 0, COLS, 0, ROWS

        numElems = 1
        while numElems <= totalElems:
            # Go right
            for i in range(l, r):
                matrix[u][i] = numElems
                numElems += 1
            u += 1

            # Go Down
            for i in range(u, d):
                matrix[i][r - 1] = numElems
                numElems += 1
            r -= 1
            
            if numElems > totalElems:
                break

            # Go Left
            for i in range(r - 1, l - 1, -1):
                matrix[d - 1][i] = numElems
                numElems += 1
            d -= 1

            # Go Up
            for i in range(d - 1, u - 1, -1):
                matrix[i][l] = numElems
                numElems += 1
            l += 1

        return matrix
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        ROWS, COLS = len(mat), len(mat[0])
        if r * c != ROWS * COLS:
            return mat

        newR, newC = 0, 0
        newMat = [[0] * c for _ in range(r)]

        for i in range(ROWS):
            for j in range(COLS):
                newMat[newR][newC] = mat[i][j]
                newC += 1
                if newC == c:
                    newC = 0
                    newR += 1
        
        return newMat

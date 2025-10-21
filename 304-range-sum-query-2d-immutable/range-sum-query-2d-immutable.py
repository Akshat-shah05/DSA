class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.rows, self.cols = len(matrix), len(matrix[0])
        for r in range(self.rows):
            for c in range(1, self.cols):
                self.matrix[r][c] += self.matrix[r][c - 1]
        
        for c in range(self.cols):
            for r in range(1, self.rows):
                self.matrix[r][c] += self.matrix[r - 1][c]

        print(self.matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        matrix = self.matrix
        squareSize = matrix[row2][col2]
        stripAboveSize = matrix[row1 - 1][col2] if (0 <= row1 - 1 < self.rows) else 0
        stripLeftSize = matrix[row2][col1 - 1] if (0 <= col1 - 1 < self.cols) else 0
        stripDoubleCounted = matrix[row1 - 1][col1 - 1] if (row1 > 0 and col1 > 0) else 0

        return squareSize - stripAboveSize - stripLeftSize + stripDoubleCounted
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
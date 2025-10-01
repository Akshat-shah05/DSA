class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        if rows == 0 or cols == 0:
            return False

        r, c = rows - 1, 0 

        while r >= 0 and c < cols:
            elem = matrix[r][c]

            if target == elem:
                return True
            
            elif target < elem:
                r -= 1
            
            else:
                c += 1
        
        return False
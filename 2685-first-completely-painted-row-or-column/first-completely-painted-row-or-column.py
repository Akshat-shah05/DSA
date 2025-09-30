class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        # set for each row, set for each column
        # see when a set is full --> return that
        rowSet = defaultdict(int)
        colSet = defaultdict(int)
        numMap = defaultdict(tuple)
        rows, cols = len(mat), len(mat[0])

        for r in range(rows):
            for c in range(cols):
                rowSet[r] += 1
                colSet[c] += 1
                numMap[mat[r][c]] = (r, c)

        for i in range(len(arr)):
            row, col = numMap[arr[i]]
            rowSet[row] -= 1
            colSet[col] -= 1

            if rowSet[row] == 0 or colSet[col] == 0:
                return i
        


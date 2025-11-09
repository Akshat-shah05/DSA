class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        n = len(board)
        colMovesNeeded = 0
        rowMovesNeeded = 0
        onesInFirstRow = 0
        onesInFirstCol = 0

        # All the cases where it is IMPOSSIBLE
        for r in range(n):
            for c in range(n):
                if (board[r][0] ^ board[0][0]) ^ (board[r][c] ^ board[0][c]):
                    return -1
        
        for i in range(n):
            onesInFirstRow += board[0][i]
            onesInFirstCol += board[i][0]
            if board[i][0] == i % 2:
                rowMovesNeeded += 1
            if board[0][i] == i % 2:
                colMovesNeeded += 1
        
        if not (n // 2 <= onesInFirstRow <= (n + 1) // 2): return -1
        if not (n // 2 <= onesInFirstCol <= (n + 1) // 2): return -1

        if n % 2 == 1:
            if (colMovesNeeded % 2 == 1):
                colMovesNeeded = n - colMovesNeeded
            if (rowMovesNeeded % 2 == 1):
                rowMovesNeeded = n - rowMovesNeeded

        else:
            colMovesNeeded = min(colMovesNeeded, n - colMovesNeeded)
            rowMovesNeeded = min(rowMovesNeeded, n - rowMovesNeeded)

        return (colMovesNeeded + rowMovesNeeded) // 2
        

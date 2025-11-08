class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def makeBoard(state):
            board = []
            for row in state:
                board.append("".join(row))
            
            return board
        
        ans = []
        def backtrack(row, diag, antidiag, cols, state):
            if row == n:
                ans.append(makeBoard(state))
            
            for col in range(n):
                curDiag = row - col
                curAntiDiag = row + col

                if col in cols or curDiag in diag or curAntiDiag in antidiag:
                    continue
                
                cols.add(col)
                diag.add(curDiag)
                antidiag.add(curAntiDiag)
                state[row][col] = "Q"

                backtrack(row + 1, diag, antidiag, cols, state)

                state[row][col] = "."
                antidiag.remove(curAntiDiag)
                diag.remove(curDiag)
                cols.remove(col)
        
        state = [["."] * n for _ in range(n)]
        backtrack(0, set(), set(), set(), state)
        return ans
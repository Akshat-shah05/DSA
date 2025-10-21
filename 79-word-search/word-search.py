class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ans = False
        n = len(word)
        rows, cols = len(board), len(board[0])
    
        def backtrack(r, c, i):
            if i == n:
                return True
            
            if not (0 <= r < rows and 0 <= c < cols) or board[r][c] != word[i]:
                return False

            ch = board[r][c]
            board[r][c] = "#"
            found = (
                backtrack(r + 1, c, i + 1) or
                backtrack(r - 1, c, i + 1) or 
                backtrack(r, c + 1, i + 1) or
                backtrack(r, c - 1, i + 1)
            )
            board[r][c] = ch
            return found

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True

        return False
    

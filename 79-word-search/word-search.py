class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        rows, cols = len(board), len(board[0])
        n = len(word)
    
        def backtrack(r, c, i):
            if i == n:
                return True

            if not 0 <= r < rows or not 0 <= c < cols or word[i] != board[r][c]:
                return False
            
            ch = board[r][c]
            board[r][c] = "#"

            for dr, dc in directions:
                if backtrack(r + dr, c + dc, i + 1):
                    return True
            
            board[r][c] = ch
            return False
        

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and backtrack(r, c, 0):
                    return True
            
        return False

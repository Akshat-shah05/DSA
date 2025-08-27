class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[None] * n for _ in range(n)]
        self.directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]
        
    def move(self, row: int, col: int, player: int) -> int:
        if self.board[row][col] is not None:
            raise ValueError("Cell already taken, try again")
        
        self.board[row][col] = player
        return player if self._checkwin(row, col, player) else 0

    
    def _checkwin(self, row, col, player):
        for dr, dc in self.directions:
            count = 1

            # move forwards
            nr, nc = row + dr, col + dc
            while 0 <= nr < self.n and 0 <= nc < self.n and self.board[nr][nc] == player:
                count += 1
                nr += dr
                nc += dc
            
            nr, nc = row - dr, col - dc
            while 0 <= nr < self.n and 0 <= nc < self.n and self.board[nr][nc] == player:
                count += 1
                nr -= dr
                nc -= dc
            
            if count >= self.n:
                return True
            
        return False
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
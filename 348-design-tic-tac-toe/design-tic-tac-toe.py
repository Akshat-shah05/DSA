class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.board = [[None] * n for _ in range(n)]
        self.directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]

    def move(self, row: int, col: int, player: int) -> int:
        if self.board[row][col] is not None:
            raise ValueError("This cell is already taken")
        
        self.board[row][col] = player
        return player if self._checkwin(row, col, player) else 0
    
    def _checkwin(self, row, col, player):
        for dr, dc in self.directions:
            count = 1
            
            # Forward Direction
            newR, newC = row + dr, col + dc
            while 0 <= newR < self.n and 0 <= newC < self.n and self.board[newR][newC] == player:
                count += 1
                newR += dr
                newC += dc
        
            # Reverse Direction
            newR, newC = row - dr, col - dc
            while 0 <= newR < self.n and 0 <= newC < self.n and self.board[newR][newC] == player:
                count += 1
                newR -= dr
                newC -= dc
            
            if count >= self.n:
                return True
        
        return False
        
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
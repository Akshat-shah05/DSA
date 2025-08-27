class TicTacToe:

    def __init__(self, n: int) -> None:
        self.n = n
        self.board = [[None] * n for _ in range(n)]
        self.directions = [(1, 0), (0, 1), (1, 1), (-1, 1)]

    def move(self, row: int, col: int, player: int) -> int:
        if self.board[row][col] is not None:
            raise ValueError("Cell already taken, try again!")
        
        self.board[row][col] = player
        return player if self._checkwin(row, col, player) else 0

    
    def _checkwin(self, row: int, col: int, player: int) -> bool:
        for dr, dc in self.directions:
            count = -1

            # Moving in the forward direction
            newRow, newCol = row, col
            while self._validRC(newRow, newCol, player):
                count += 1
                newRow += dr
                newCol += dc
            
            # Moving in the backwards direction
            newRow, newCol = row, col
            while self._validRC(newRow, newCol, player):
                count += 1
                newRow -= dr
                newCol -= dc
            
            if count >= self.n:
                return True
        
        return False
    
    def _validRC(self, row, col, player):
        return 0 <= row < self.n and 0 <= col < self.n and self.board[row][col] == player
            

        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
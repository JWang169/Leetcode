class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        
        self.col = [0] * n
        self.row = [0] * n
        self.n = n
        self.diag, self.anti = 0, 0
        
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        if player == 1:
            c = 1
        else:
            c = -1
        self.col[col] += c
        self.row[row] += c
        if row == col:
            self.diag += c
        if row + col == self.n - 1:
            self.anti += c 
            
        target = c * self.n
        if self.col[col] == target or self.row[row] == target or self.anti == target or self.diag == target:
            return player
        return 0
        
        
        
        

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
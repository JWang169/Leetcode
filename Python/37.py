class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.dfs(0, 0)
        
    def dfs(self, i, j):
        chars = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        if i == 9:
            return True 
        if j == 9:
            return self.dfs(i + 1, 0)
        if self.board[i][j] != '.':
            return self.dfs(i, j + 1)
        for ch in chars:
            if not self.isValid(i, j, ch):
                continue
            self.board[i][j] = ch 
            if self.dfs(i, j + 1):
                return True 
            self.board[i][j] = '.'
        return False 
    
    
    def isValid(self, i, j, ch):
        for x in range(9):
            if self.board[x][j] == ch:
                return False 
        for y in range(9):
            if self.board[i][y] == ch:
                return False 
        nx = i // 3 * 3
        ny = j // 3 * 3
        for x in range(3):
            for y in range(3):
                if self.board[nx + x][ny + y] == ch:
                    return False
        return True 
                
            
        
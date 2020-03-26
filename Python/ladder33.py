class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.results = []
        self.dfs([], n)
        print(self.results)
        boards = []
        
        for result in self.results:
            board = []
            for i in range(n):
                row = ['.'] * n
                row[result[i]] = 'Q'
                board.append(''.join(row))
            boards.append(board)
        return boards
        
    def dfs(self, prev, n):
        if len(prev) == n:
            self.results.append(prev)
            return 
        
        
        # try every col in this row
        i = len(prev) 
        for j in range(n):
            valid = True
            for row, col in enumerate(prev):
                # same column, diagonal
                if col == j or abs(i - row) == abs(j - col):
                    valid = False
                    break
                    
            if valid:
                self.dfs(prev + [j], n) 
    
                    
            
        
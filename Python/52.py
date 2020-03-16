class Solution:
    def totalNQueens(self, n: int) -> int:
        self.results = 0
        self.dfs([], n)
        return self.results
    
    def dfs(self, prev, n):
        if len(prev) == n:
            self.results += 1 
            return 
        newRow = len(prev)
        for newCol in range(n):
            isValid = True
            for preRow, preCol in enumerate(prev):
                if preCol == newCol or abs(preCol - newCol) == abs(preRow - newRow):
                    isValid = False
            if isValid:
                self.dfs(prev + [newCol], n)